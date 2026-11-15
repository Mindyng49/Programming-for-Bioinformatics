import pytest
from lab02_sequences import find_motif

def test_find_motif():
    # Test case 1: Basic
    result = find_motif("ATGCATG","ATG")
    assert result == [0,4]

    #Test case 2: Overlapping motifs
    result = find_motif("AAAA","AA")
    assert result == [0,1,2]

    #Test case 3: Motif not found
    result = find_motif("ATGCATG","CCC")
    assert result == []
