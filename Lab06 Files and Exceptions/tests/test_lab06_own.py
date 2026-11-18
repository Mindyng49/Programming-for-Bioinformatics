import pytest

from src.bio_io import FastaFormatError, read_fasta
from src.batch import process_directory, main

def test_empty_fasta_file(tmp_path):
    fasta_file = tmp_path / "empty.fasta"
    fasta_file.write_text("")

    result = process_directory(
        tmp_path,
        tmp_path / "output.csv"
    )

    assert result == {
        "processed": 0,
        "rejected": 1,
        "records": 0
    }

def test_missing_fasta_file(tmp_path):
    missing_file = tmp_path / "missing.fasta"

    with pytest.raises(OSError):
        list(read_fasta(missing_file))

def test_fasta_record_without_sequence(tmp_path):
    fasta_file = tmp_path / "no_sequence.fasta"
    fasta_file.write_text(">gene1\n")

    with pytest.raises(FastaFormatError):
        list(read_fasta(fasta_file))

def test_main_missing_folder(tmp_path, capsys):
    missing_folder = tmp_path / "not_exist"

    result = main([str(missing_folder)])

    captured = capsys.readouterr()

    assert result == 2
    assert "error" in captured.err.lower()