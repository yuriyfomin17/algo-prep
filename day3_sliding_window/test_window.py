import time

from day3_sliding_window.window import (
    RateLimiter,
    longest_unique_run,
    max_events_in_window,
    min_len_sum_at_least,
)


def test_rate_limiter_basic():
    rl = RateLimiter(limit=3, window=1.0)
    assert [rl.allow(t) for t in (0.0, 0.1, 0.2, 0.3)] == [True, True, True, False]


def test_rate_limiter_expiry_is_exclusive():
    rl = RateLimiter(limit=2, window=1.0)
    assert rl.allow(0.0) and rl.allow(0.5)
    assert not rl.allow(0.99)
    assert rl.allow(1.0)  # event at 0.0 is exactly 1s old -> expired
    assert not rl.allow(1.2)
    assert rl.allow(1.5)


def test_rate_limiter_rejected_do_not_count():
    rl = RateLimiter(limit=1, window=10.0)
    assert rl.allow(0)
    assert not any(rl.allow(t) for t in range(1, 10))
    assert rl.allow(10)


def test_rate_limiter_is_fast():
    rl = RateLimiter(limit=1000, window=1.0)
    start = time.perf_counter()
    for i in range(200_000):
        rl.allow(i / 1000)
    assert time.perf_counter() - start < 2.0


def test_max_events_in_window():
    assert max_events_in_window([], 1.0) == 0
    assert max_events_in_window([5.0], 1.0) == 1
    assert max_events_in_window([0, 1, 2, 3], 1.0) == 2  # closed interval
    assert max_events_in_window([0, 0.1, 0.2, 5, 5.1, 5.2, 5.3], 0.5) == 4


def test_longest_unique_run():
    assert longest_unique_run("") == 0
    assert longest_unique_run("abcabcbb") == 3
    assert longest_unique_run("bbbb") == 1
    assert longest_unique_run("pwwkew") == 3
    assert longest_unique_run("abba") == 2


def test_min_len_sum_at_least():
    assert min_len_sum_at_least([2, 3, 1, 2, 4, 3], 7) == 2
    assert min_len_sum_at_least([1, 4, 4], 4) == 1
    assert min_len_sum_at_least([1, 1, 1], 10) == 0
    assert min_len_sum_at_least([], 1) == 0
