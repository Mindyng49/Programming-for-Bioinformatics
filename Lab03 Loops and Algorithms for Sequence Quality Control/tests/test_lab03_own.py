import pytest
from src.qc import classify_read,trim_low_quality

Cases = [(640, 3, 72.4, "review"), (500, 10, 45.0, "pass")]

def test_classify_read():
    for length,n_count,gc,output in Cases:
        assert classify_read(length, n_count,gc)==output

def test_trim_low_quality():
    assert trim_low_quality([30, 10, 35, 8]) == 3