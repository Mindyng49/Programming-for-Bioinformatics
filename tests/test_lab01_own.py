import pytest
from src.basics import gc_percent, parse_counts

@pytest.mark.parametrize(
    "counts, expected",
    [((0, 50, 15, 0), 100.0)],
)
def test_boundary(counts, expected):
    assert gc_percent(*counts) == pytest.approx(expected)

def test_zero_total():
    with pytest.raises(ValueError):
        gc_percent(0, 0, 0, 0)

def test_invalid_input():
    with pytest.raises(ValueError):
        parse_counts("10 20 -5 10")