from panel import Variant, sort_variants, sorted_copy
from lookup import kmer_counts, safe_expression


def test_sorted_copy():
    old = ["TP53", "BRCA1"]
    assert sorted_copy(old) == ["BRCA1", "TP53"]
    assert old == ["TP53", "BRCA1"]


def test_chromosome_sort_variants():
    vs = [
        Variant("X", 50, "C", "T"),
        Variant("10", 20, "G", "A"),
        Variant("2", 30, "T", "C"),
        Variant("M", 100, "A", "G"),
        ]
    assert sort_variants(vs) == [
        Variant("2", 30, "T", "C"),
        Variant("10", 20, "G", "A"),
        Variant("X", 50, "C", "T"),
        Variant("M", 100, "A", "G"),
        ]


def test_kmer_counts():
    assert kmer_counts("ATG", 5) == {}
    assert kmer_counts("", 3) == {}


def test_safe_expression():
    assert safe_expression({"TP53": 0.0}, "TP53") == 0.0
    assert safe_expression({"TP53": 0.0}, "BRCA1") is None
