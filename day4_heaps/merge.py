"""Day 4 — heapq & bisect."""
from collections.abc import Iterable, Iterator


def merge_sorted_streams(*streams: Iterable[tuple]) -> Iterator[tuple]:
    """K-way merge of streams already sorted by their FIRST element (a timestamp).

    Items are tuples like (ts, venue, price); order by ts only — never compare
    the other fields. On equal ts, the item from the lower-index stream comes
    first. Must be lazy: streams may be infinite generators.
    Don't use heapq.merge — build it with heappush/heappop.
    """
    raise NotImplementedError


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping or touching [start, end] intervals. Input may be unsorted.
    (1, 3) and (3, 5) touch -> (1, 5)."""
    raise NotImplementedError


def count_in_range(sorted_vals: list[float], lo: float, hi: float) -> int:
    """How many values v satisfy lo <= v <= hi. O(log n)."""
    raise NotImplementedError
