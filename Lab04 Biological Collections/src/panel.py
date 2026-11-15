"""Lab 4 - lists and tuples for a gene panel and variant records."""
from typing import NamedTuple


class Variant(NamedTuple):
    """One variant coordinate: an immutable record with named fields."""

    chrom: str
    pos: int
    ref: str
    alt: str


def filter_panel(genes: list[str], priority: set[str]) -> list[str]:
    """Keep the genes that are in priority, preserving the original order."""
    result = []
    for gene in genes:
        if gene in priority:
            result.append(gene)
    return result


def sorted_copy(items: list) -> list:
    """Return a sorted copy; the original list is not changed."""
    return sorted(items)

    
def _chrom_key(chrom: str) -> tuple:
    chrom = chrom.removeprefix("chr").upper()
    if chrom == "X":
        return (23,)
    elif chrom == "Y":
        return (24,)
    elif chrom == "M":
        return (25,)
    else:
        return (int(chrom),)


def sort_variants(variants: list[Variant]) -> list[Variant]:
    return sorted(variants,key = lambda v:(_chrom_key(v.chrom),v.pos))