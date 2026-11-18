"""Reusable DNA sequence utilities for BioPyLearn."""

DNA_BASES = frozenset("ACGT")
COMPLEMENT = str.maketrans("ACGT", "TGCA")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    return "".join(ch for ch in raw.upper() if ch.isalpha())


def is_valid_dna(sequence: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (N if allowed)."""
    sequence = sequence.upper()
    if not sequence:
        return False
    if allow_n:
        allowed = DNA_BASES | {"N"}
    else:
        allowed = DNA_BASES
    return set(sequence) <= allowed 


def gc_content(sequence: str) -> float:
    """Return GC percentage (0-100); ValueError if invalid."""
    sequence = sequence.upper()

    if not sequence:
        raise ValueError("Empty sequence")
    if not is_valid_dna(sequence):
        raise ValueError(f"invalid DNA sequence: {sequence!r}")
    return (sequence.count("G") +  sequence.count("C"))/len(sequence) * 100


def reverse_complement(sequence: str) -> str:
    """Return the reverse complement; ValueError if invalid."""
    sequence = sequence.upper()
    if not is_valid_dna(sequence):
        raise ValueError(f"invalid DNA sequence: {sequence!r}")
    return sequence.translate(COMPLEMENT)[::-1]


def find_motif(sequence: str, motif: str) -> list[int]:
    """Return every 0-based start of motif (overlaps allowed)."""
    sequence = sequence.upper()
    motif = motif.upper()
    if not motif:
        raise ValueError("Motif cannot be empty")
    position = []
    start = sequence.find(motif)
    while start != -1:
        position.append(start)
        start = sequence.find(motif,start +1)

    return position
