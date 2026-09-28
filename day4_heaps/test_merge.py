import itertools

from day4_heaps.merge import count_in_range, merge_intervals, merge_sorted_streams


class NoCompare:
    """Payload that blows up if the merge compares it."""

    def __lt__(self, other):
        raise AssertionError("payload was compared")

    __gt__ = __le__ = __ge__ = __lt__


def test_merge_basic():
    a = [(1, "A"), (4, "A"), (9, "A")]
    b = [(2, "B"), (3, "B"), (10, "B")]
    c = []
    assert [t for t, _ in merge_sorted_streams(a, b, c)] == [1, 2, 3, 4, 9, 10]


def test_merge_ties_by_stream_index_and_no_payload_compare():
    p = NoCompare()
    a = [(1, p), (2, p)]
    b = [(1, p), (2, p)]
    out = list(merge_sorted_streams(b, a))
    assert [x[0] for x in out] == [1, 1, 2, 2]


def test_merge_tie_order():
    a = [(1, "a")]
    b = [(1, "b")]
    assert list(merge_sorted_streams(b, a)) == [(1, "b"), (1, "a")]


def test_merge_is_lazy_with_infinite_streams():
    evens = ((i, "even") for i in itertools.count(0, 2))
    odds = ((i, "odd") for i in itertools.count(1, 2))
    first = list(itertools.islice(merge_sorted_streams(evens, odds), 6))
    assert [t for t, _ in first] == [0, 1, 2, 3, 4, 5]


def test_merge_intervals():
    assert merge_intervals([]) == []
    assert merge_intervals([(8, 10), (1, 3), (2, 6), (15, 18)]) == [(1, 6), (8, 10), (15, 18)]
    assert merge_intervals([(1, 3), (3, 5)]) == [(1, 5)]
    assert merge_intervals([(1, 10), (2, 3), (4, 5)]) == [(1, 10)]


def test_count_in_range():
    vals = [1, 2, 2, 2, 5, 7, 9]
    assert count_in_range(vals, 2, 2) == 3
    assert count_in_range(vals, 0, 100) == 7
    assert count_in_range(vals, 3, 4) == 0
    assert count_in_range(vals, 5, 9) == 3
    assert count_in_range([], 0, 1) == 0
