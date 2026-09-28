"""Day 4 — LRU cache, twice.

Both classes share the same contract:
    get(key, default=None) -> value, and marks key most-recently-used
    put(key, value)        -> insert/update, marks key MRU; evicts the LRU key
                              when size would exceed capacity
    len(cache)             -> current size
Both get and put must be O(1).
"""


class LRUCacheOD:
    """Implementation #1: collections.OrderedDict (move_to_end, popitem)."""

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key, default=None):
        raise NotImplementedError

    def put(self, key, value) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError


class LRUCache:
    """Implementation #2: plain dict + your own doubly linked list (no OrderedDict).
    This is the version interviewers usually want."""

    def __init__(self, capacity: int) -> None:
        raise NotImplementedError

    def get(self, key, default=None):
        raise NotImplementedError

    def put(self, key, value) -> None:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError
