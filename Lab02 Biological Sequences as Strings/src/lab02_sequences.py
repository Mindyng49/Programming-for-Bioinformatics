"""Lab 2 - biological sequences as strings (becomes sequence_utils.py in Week 5)."""

DNA_BASES = frozenset("ACGT")


def clean_sequence(raw: str) -> str:
    """Upper-case raw text and drop spaces, digits and newlines."""
    return "".join(ch for ch in raw.upper() if ch.isalpha())

def is_valid_dna(seq: str, allow_n: bool = False) -> bool:
    """True for a non-empty string of A, C, G, T (and N when allowed)."""
    if not seq:
        return False
    if allow_n:
        allowed = DNA_BASES |{"N"}
    else:
        allowed = DNA_BASES
    return set(seq)<= allowed 


def gc_content(seq: str) -> float:
    """Return GC percentage (0-100); ValueError if empty or not A/C/G/T."""
    seq = seq.upper()

    if not seq:
        raise ValueError("Empty sequence")
    if not is_valid_dna(seq):
        raise ValueError("Invalid DNA sequence")
    return (seq.count("G") +  seq.count("C"))/len(seq) * 100

def transcribe(dna: str) -> str:
    """Return the RNA copy of a DNA sequence (T becomes U)."""
    if not is_valid_dna(dna):
        raise ValueError("Invalid DNA sequence")
    return dna.upper().replace("T","U")


def find_motif(seq: str, motif: str) -> list[int]:
    """Return every 0-based start of motif in seq (overlaps allowed)."""
    seq = seq.upper()
    motif = motif.upper()
    if not motif:
        raise ValueError("Motif cannot be empty")
    position = []
    start = seq.find(motif)
    while start != -1:
        position.append(start)
        start = seq.find(motif,start +1)

    return position

