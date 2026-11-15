"""Lab 1 - Python fundamentals for biological calculations."""


def gc_percent(a: int, c: int, g: int, t: int) -> float:
    """Return the GC percentage from the four base counts.

    Raises:
        ValueError: if any count is negative or the total is zero.
    """

    """ raise NotImplementedError("TODO: implement gc_percent")"""
    if a < 0 or c < 0 or g < 0 or t < 0:
        raise ValueError("Base counts cannot be negative numbers")

    total = a + c + g + t
    if total == 0:
        raise ValueError("Total base count is zero")

    return ((c + g) / total) * 100


def format_report(sample: str, length: int, gc: float) -> str:
    """Return a one-line report with units, e.g. 'S1: 60 bases, GC 46.7%'."""
    """raise NotImplementedError("TODO: implement format_report")"""
    return f"{sample}: {length} bases, GC {gc:.1f}%"

def parse_counts(text: str) -> tuple[int, int, int, int]:
    """Parse 'A C G T' counts separated by spaces or commas.

    Raises:
        ValueError: if there are not exactly four non-negative integers.
    """
    """raise NotImplementedError("TODO: implement parse_counts")"""
    parts = text.replace(","," ").split()

    if len(parts) != 4:
        raise ValueError("Input must contain 4 values")

    try:
        parse_counts = [int(x) for x in parts]
    except ValueError:
        raise ValueError("All counts must be integers")

    if any(count < 0 for count in parse_counts):
        raise ValueError("All counts must be non-negative integers")

    return tuple(parse_counts)