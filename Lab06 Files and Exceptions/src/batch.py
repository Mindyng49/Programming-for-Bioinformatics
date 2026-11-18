"""Week 6 extension - batch processing, logging, FASTQ and a command-line tool."""
import argparse
import logging
import sys
from collections.abc import Iterator
from pathlib import Path

from bio_io import FastaFormatError, read_fasta, write_csv

LOG = logging.getLogger("batch")


class FastqFormatError(ValueError):
    """Raised when a FASTQ file is malformed."""


def process_directory(in_dir, out_csv, log_path=None) -> dict[str, int]:
    """Read every *.fasta file in in_dir; one bad file never stops the batch.

    Writes one row per file (file, records, status, reason) to out_csv and
    returns {'processed': ..., 'rejected': ..., 'records': ...}.
    """
    handler = None
    if log_path is not None:
        Path(log_path).parent.mkdir(parents=True, exist_ok=True)
        handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
        LOG.addHandler(handler)
        LOG.setLevel(logging.INFO)
    rows: list[dict] = []
    summary = {"processed": 0, "rejected": 0, "records": 0}

    files = sorted(Path(in_dir).glob("*.fasta"))
    try:
        for file in files:
            try:
                file_records = list(read_fasta(file))
                if not file_records:
                    summary["rejected"] += 1
                    rows.append({"file": file.name, "records": 0, "status": "rejected", "reason": "empty file"})
                    LOG.warning("%s empty file", file.name)
                    continue
                count = len(file_records)
                summary["processed"] += 1
                summary["records"] += count
                rows.append({"file": file.name, "records": count, "status": "processed", "reason": ""})
                LOG.info("%s processed", file.name)
            except (OSError, UnicodeDecodeError, FastaFormatError) as error:
                summary["rejected"] += 1
                rows.append({"file": file.name, "records": 0, "status": "rejected", "reason": str(error)})
                LOG.warning("%s %s", file.name, error)
    finally:
        if handler is not None:
            LOG.removeHandler(handler)
            handler.close()
    
    Path(out_csv).parent.mkdir(parents=True, exist_ok=True)
    write_csv(rows, out_csv, ["file", "records", "status", "reason"])

    return summary

def read_fastq(path) -> Iterator[tuple[str, str, str]]:
    """Yield (read_id, sequence, quality) for each 4-line FASTQ record."""
    with open(path, "r", encoding="utf-8") as handle:
        while True:
            header = handle.readline()
            if not header:
                break
            header = header.strip()
            if not header:
                continue
            seq = handle.readline().strip()
            plus = handle.readline().strip()
            quality = handle.readline().strip()
            if not header.startswith("@") or not plus.startswith("+"):
                raise FastqFormatError("Invalid FASTQ format")
            if len(seq) != len(quality):
                raise FastqFormatError(f"{path}: sequence and quality lengths differ " f"for {header.strip() !r}")
            
            read_id = header[1:].split()[0]
            yield read_id, seq, quality

def mean_phred(quality: str, offset: int = 33) -> float:
    """Mean Phred score of a quality string (Phred+33 by default)."""
    if not quality:
        raise ValueError("quality string is empty")
    
    scores = [ord(ch) - offset for ch in quality]
    return sum(scores) / len(scores)


def main(argv: list[str] | None = None) -> int:
    """Command-line entry point. Exit code 0 = all good, 1 = some files rejected, 2 = bad input."""
    parser = argparse.ArgumentParser()
    parser.add_argument("in_dir", help="Input folder containing FASTA files")
    parser.add_argument("--out", default="results", help="Output folder")
    args = parser.parse_args(argv)
    if not Path(args.in_dir).is_dir():
        print(f"error: {args.in_dir} is not a folder", file=sys.stderr)
        return 2
    
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_csv = out_dir / "processing_log.csv"
    log_path = out_dir / "batch.log"

    summary = process_directory(args.in_dir, out_csv, log_path)
    print(
        f"processed={summary['processed']} "
        f"rejected={summary['rejected']} "
        f"records={summary['records']}"
    )

    if summary["rejected"] > 0:
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
