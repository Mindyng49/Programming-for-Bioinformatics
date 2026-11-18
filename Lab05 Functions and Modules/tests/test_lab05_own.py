import pytest

from normalize import proportions,cpm
from sequence_utils import clean_sequence, find_motif, gc_content, is_valid_dna, reverse_complement

def test_input_is_not_changed():
    raw = [120,80,40]
    result = proportions(raw)
    assert raw == [120,80,40]
    assert sum(result) == pytest.approx(1.0)


def zero_total():
    with pytest.raises(ValueError, match="zero"):
        proportions([0, 0, 0])


def test_clean_sequence():
    assert clean_sequence("atg 123 c") == "ATGC"


def test_reverse_complement():
    assert reverse_complement("ATGC") == "GCAT"