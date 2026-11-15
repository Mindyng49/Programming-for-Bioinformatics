"""Lab 3 - sequence quality control with conditions and loops."""


def classify_read(
    length: int,
    n_count: int,
    gc: float,
    *,
    min_len: int = 500,
    max_n: int = 10,
    gc_range: tuple[float, float] = (30.0, 70.0),
) -> str:
    """Return 'reject', 'review' or 'pass' for one sequencing record.

    Rules are checked in this order: too short -> reject; too many N or GC
    outside the inclusive range -> review; otherwise pass.
    """
    if length < min_len:
        return "reject"
    if n_count > max_n or gc < gc_range[0] or gc > gc_range[1]:
        return "review"
    return "pass"


def qc_summary(records: list[dict]) -> dict[str, int]:
    """Count records per decision. Values may be numbers or CSV strings."""
    counts = {"reject": 0, "review":0, "pass": 0}
    for rec in records:
        length = int(rec["length"])
        n_count = int(rec["n_count"])
        gc = float(rec["gc_percent"])
        decision = classify_read(length,n_count,gc)

        counts[decision] +=1
    return counts

def trim_low_quality(quals: list[int], threshold: int = 20) -> int:
    """Return how many bases to keep after trimming a low-quality 3' tail."""
    end = len(quals)

    while end>0 and quals[end-1] < threshold:
        end -=1
    return end