"""Bounded, local structure inspection. Never emits raw values or relationships.

Python 3.11+. Optional readers: pyarrow (Parquet), h5py (HDF5/NWB).
CSV/TSV sampling requires explicit columns; all other formats are metadata/schema only.
This tool is not an access-control boundary or an answerability validator.
"""

from __future__ import annotations

import argparse
import csv
import importlib
import json
import re
import sys
from pathlib import Path


class ProfileError(Exception):
    """A limitation that must not be interpreted as a dataset fact."""


def require(module: str):
    try:
        return importlib.import_module(module)
    except ImportError as exc:
        raise ProfileError(f"Optional dependency unavailable: {module}") from exc


def scalar_type(value: str) -> str:
    if value.lower() in {"true", "false"}:
        return "boolean-like"
    if re.fullmatch(r"[+-]?\d+", value):
        return "integer-like"
    try:
        float(value)
        return "number-like"
    except ValueError:
        return "text"


def bounded_lines(handle, max_bytes: int):
    remaining = max_bytes
    while True:
        line = handle.readline(remaining + 1)
        if len(line) > remaining:
            raise ProfileError(
                "Read budget reached before a complete record; raise --max-bytes only within authorized scope"
            )
        if not line:
            return
        remaining -= len(line)
        yield line.decode("utf-8-sig" if handle.tell() == len(line) else "utf-8")


def table(path: Path, args) -> dict:
    delimiter = "\t" if path.suffix.lower() == ".tsv" else ","
    with path.open("rb") as handle:
        reader = csv.reader(
            bounded_lines(handle, args.max_bytes), delimiter=delimiter, strict=True
        )
        header = next(reader, None)
        if (
            not header
            or any(not key for key in header)
            or len(set(header)) != len(header)
        ):
            raise ProfileError(
                "Header is empty, contains empty names, or has duplicate names; clarify the schema"
            )
        output = {
            "format": "tsv" if delimiter == "\t" else "csv",
            "columns": header,
            "row_count": None,
            "scope": "header only; values not summarized",
        }
        if not args.sample_rows:
            return output
        selected = args.columns.split(",")
        if len(set(selected)) != len(selected) or any(
            key not in header for key in selected
        ):
            raise ProfileError(
                "Requested columns must be unique and present in the header"
            )
        indices = [(key, header.index(key)) for key in selected]
        stats = {key: {"empty_count": 0, "lexical_types": []} for key in selected}
        types = {key: set() for key in selected}
        count, complete = 0, False
        while count < args.sample_rows:
            row = next(reader, None)
            if row is None:
                complete = True
                break
            if len(row) != len(header):
                raise ProfileError(
                    "A sampled record has the wrong field count; no statistics reported"
                )
            count += 1
            for key, index in indices:
                value = row[index]
                if value == "":
                    stats[key]["empty_count"] += 1
                else:
                    types[key].add(scalar_type(value))
        for key in selected:
            stats[key]["lexical_types"] = sorted(types[key])
        output.update(
            {
                "scope": "explicit selected-column prefix",
                "rows_inspected": count,
                "row_count": count if complete else None,
                "end_of_file_observed": complete,
                "selected_columns": stats,
                "missingness_policy": "empty string only; sentinels and semantic missingness unknown",
                "sample_limit": args.sample_rows,
            }
        )
        return output


def read_json(path: Path, max_bytes: int):
    with path.open("rb") as handle:
        raw = handle.read(max_bytes + 1)
    if len(raw) > max_bytes:
        raise ProfileError("JSON metadata exceeds --max-bytes; no partial parse used")
    return json.loads(raw)


def json_shape(value, budget: list[int], depth: int = 0):
    if budget[0] <= 0 or depth > 8:
        return {"type": "uninspected", "reason": "schema budget"}
    budget[0] -= 1
    if isinstance(value, dict):
        result = {"type": "object", "key_count": len(value), "properties": {}}
        for key, item in value.items():
            if budget[0] <= 0:
                result["properties_truncated"] = True
                break
            result["properties"][key] = json_shape(item, budget, depth + 1)
        return result
    if isinstance(value, list):
        return {
            "type": "array",
            "length": len(value),
            "first_item_schema": json_shape(value[0], budget, depth + 1)
            if value
            else None,
            "item_schema_scope": "first item only; heterogeneity unknown",
        }
    return {"type": "null" if value is None else type(value).__name__}


def json_document(path: Path, args) -> dict:
    if path.suffix.lower() in {".jsonl", ".ndjson"}:
        with path.open("rb") as handle:
            line = handle.readline(args.max_bytes + 1)
        if len(line) > args.max_bytes:
            raise ProfileError("First JSONL record exceeds --max-bytes")
        if not line.strip():
            raise ProfileError("First JSONL record is empty; schema unknown")
        value = json.loads(line)
        scope = "first JSONL record only; no population row count or raw values"
    else:
        value = read_json(path, args.max_bytes)
        scope = "bounded JSON document; nested array schema from first item only"
    return {
        "format": path.suffix.lower().lstrip("."),
        "scope": scope,
        "schema": json_shape(value, [args.max_nodes]),
    }


def parquet(path: Path, args) -> dict:
    pq = require("pyarrow.parquet")
    with pq.ParquetFile(path) as file:
        fields = list(file.schema_arrow)
        return {
            "format": "parquet",
            "scope": "footer schema and counts only; no row-group statistics",
            "row_count": file.metadata.num_rows,
            "columns": [
                {
                    "name": field.name,
                    "type": str(field.type),
                    "nullable": field.nullable,
                }
                for field in fields[: args.max_nodes]
            ],
            "columns_truncated": len(fields) > args.max_nodes,
        }


def hdf5(path: Path, args) -> dict:
    h5 = require("h5py")
    nodes, seen = [], set()
    truncated = False
    with h5.File(path, "r") as file:
        stack = [file]
        while stack:
            group = stack.pop()
            address = h5.h5o.get_info(group.id).addr
            if address in seen:
                continue
            seen.add(address)
            for name in group:
                if len(nodes) >= args.max_nodes:
                    truncated = True
                    break
                full = group.name.rstrip("/") + "/" + name
                link = group.get(name, getlink=True)
                if not isinstance(link, h5.HardLink):
                    nodes.append(
                        {"path": full, "kind": "link", "status": "not followed"}
                    )
                    continue
                obj = group[name]
                if isinstance(obj, h5.Group):
                    nodes.append({"path": full, "kind": "group"})
                    stack.append(obj)
                elif isinstance(obj, h5.Datatype):
                    nodes.append(
                        {"path": full, "kind": "datatype", "dtype": str(obj.dtype)}
                    )
                else:
                    nodes.append(
                        {
                            "path": full,
                            "kind": "array",
                            "shape": obj.shape,
                            "dtype": str(obj.dtype),
                        }
                    )
            if truncated:
                break
    return {
        "format": "hdf5",
        "scope": "local object names, shapes and dtypes; no attributes, arrays or external links",
        "nodes": nodes,
        "truncated": truncated,
    }


def zarr_metadata(path: Path, args) -> dict:
    import os

    if not any((path / name).is_file() for name in (".zarray", ".zgroup", "zarr.json")):
        raise ProfileError("Directory is not a recognized local Zarr store")
    nodes, stack, visits = [], [path], 0
    truncated = False
    while stack:
        folder = stack.pop()
        for name in (".zarray", ".zgroup", "zarr.json"):
            p = folder / name
            if p.is_symlink():
                raise ProfileError("Symlinked Zarr metadata is not followed")
            if p.is_file():
                meta = read_json(p, args.max_bytes)
                nodes.append(
                    {
                        "path": str(folder.relative_to(path)),
                        "metadata_file": name,
                        "shape": meta.get("shape"),
                        "dtype": meta.get("dtype", meta.get("data_type")),
                        "kind": meta.get(
                            "node_type", "array" if name == ".zarray" else "group"
                        ),
                    }
                )
        with os.scandir(folder) as entries:
            for item in entries:
                visits += 1
                if visits >= args.max_nodes:
                    truncated = True
                    break
                if item.is_dir(follow_symlinks=False):
                    # Chunk directories contain no metadata and need not be explored.
                    child = Path(item.path)
                    if any(
                        (child / name).is_file()
                        for name in (".zarray", ".zgroup", "zarr.json")
                    ):
                        stack.append(child)
            if truncated:
                break
    return {
        "format": "zarr",
        "scope": "local metadata only; no attributes or chunks",
        "nodes": nodes,
        "truncated": truncated,
        "directory_entries_seen": visits,
    }


def inspect(path: Path, args) -> dict:
    if path.is_symlink():
        raise ProfileError(
            "Select the authorized source explicitly; input symlinks are not followed"
        )
    if not path.exists():
        raise ProfileError("Input is unavailable; no claim about dataset contents")
    suffix = path.suffix.lower()
    if args.sample_rows and suffix not in {".csv", ".tsv"}:
        raise ProfileError(
            "Bounded selected-column scans are implemented only for CSV/TSV"
        )
    if path.is_dir():
        result = zarr_metadata(path, args)
    elif suffix in {".csv", ".tsv"}:
        result = table(path, args)
    elif suffix in {".json", ".jsonl", ".ndjson"}:
        result = json_document(path, args)
    elif suffix in {".parquet", ".pqt"}:
        result = parquet(path, args)
    elif suffix in {".h5", ".hdf5", ".nwb"}:
        result = hdf5(path, args)
    else:
        raise ProfileError(
            "Unsupported format; use documentation or a reviewed local reader, not automatic deserialization"
        )
    return {
        "source": str(path.resolve()),
        "evidence_kind": "observed",
        "scientific_answerability": "not assessed",
        **result,
    }


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument(
        "--sample-rows",
        type=int,
        default=0,
        help="CSV/TSV only, 0..10000; requires --columns",
    )
    parser.add_argument(
        "--columns",
        help="Comma-separated authorized columns; no values are printed",
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=1048576,
        help="Read budget for text or each metadata document",
    )
    parser.add_argument(
        "--max-nodes", type=int, default=1000, help="Schema/object traversal budget"
    )
    args = parser.parse_args(argv)
    if not 0 <= args.sample_rows <= 10000 or args.max_bytes < 1 or args.max_nodes < 1:
        parser.error("Limits must be positive; sample rows must be 0..10000")
    if bool(args.sample_rows) != bool(args.columns):
        parser.error("--sample-rows and --columns must be used together")
    try:
        result = inspect(args.path, args)
    except ProfileError as exc:
        print(
            json.dumps({"status": "not_inspected", "reason": str(exc)}), file=sys.stderr
        )
        return 2
    except (OSError, ValueError, csv.Error, RuntimeError, KeyError, TypeError) as exc:
        # Do not echo malformed input, raw records, attributes or signed URLs.
        print(
            json.dumps(
                {
                    "status": "not_inspected",
                    "reason": f"Read/format error ({type(exc).__name__}); inspect schema within authorized scope",
                }
            ),
            file=sys.stderr,
        )
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
