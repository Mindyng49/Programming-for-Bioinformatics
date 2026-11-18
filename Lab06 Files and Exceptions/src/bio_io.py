"""Week 6 - reading FASTA and CSV safely."""
import csv
from collections.abc import Iterator
from pathlib import Path


class FastaFormatError(ValueError):
    """Raised when a FASTA file does not follow the format."""


def _finish(record_id: str, chunks: list[str], path) -> tuple[str, str]:
    sequence = "".join(chunks).upper()
    if not record_id or not sequence:
        raise FastaFormatError(f"{path}: record {record_id} is missing required fields")
    return record_id, sequence


def read_fasta(path) -> Iterator[tuple[str, str]]:
    """Yield (record_id, sequence) for every record in a FASTA file.

    The id is the first word of the header. Wrapped lines are joined and the
    sequence is upper-cased. Records are produced one at a time, so large
    files do not have to fit in memory.

    Raises:
        FileNotFoundError: if the file does not exist.
        FastaFormatError: for data before the first header, an empty header
            or a record without sequence.
    """
    with open(path, encoding="utf-8") as file:
        record_id = None
        chunks = []

        for line in file:
            line = line.strip()
            if not line:
                continue

            if line.startswith(">"):
                if not line[1:].split():
                    raise FastaFormatError(f"{path}: empty header")
                if record_id is not None:
                    yield _finish(record_id, chunks, path)
                chunks = []
                record_id = line[1:].split()[0]
                    
            else:
                if record_id is None:
                    raise FastaFormatError(f"{path}: data before first header")
                chunks.append(line)

        if record_id is not None:
            yield _finish(record_id, chunks, path)


def read_csv_records(path) -> list[dict[str, str]]:
    """Read a CSV file into a list of dictionaries (all values are strings)."""
    with open(path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(rows: list[dict], path, fieldnames: list[str]) -> None:
    """Write rows to a CSV file, creating the parent folder if needed."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
