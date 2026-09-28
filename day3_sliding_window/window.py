"""Day 3 — two pointers & sliding window (collections.deque)."""


class RateLimiter:
    """Allow at most `limit` events in any sliding window of `window` seconds.

    allow(ts) is called with non-decreasing timestamps. An accepted event at
    time t counts for the half-open window (ts - window, ts]; i.e. an event
    exactly `window` seconds old has already expired.
    Rejected events do NOT count toward the limit.
    allow() must be amortised O(1).
    """

    def __init__(self, limit: int, window: float) -> None:
        raise NotImplementedError

    def allow(self, ts: float) -> bool:
        raise NotImplementedError


def max_events_in_window(timestamps: list[float], window: float) -> int:
    """timestamps sorted ascending. Return the max number of events inside any
    closed interval [t, t + window]. O(n)."""
    raise NotImplementedError


def longest_unique_run(s: str) -> int:
    """Length of the longest substring without repeating characters. O(n)."""
    raise NotImplementedError


def min_len_sum_at_least(nums: list[int], target: int) -> int:
    """nums are positive. Length of the shortest contiguous subarray whose sum
    is >= target, or 0 if none. O(n)."""
    raise NotImplementedError
