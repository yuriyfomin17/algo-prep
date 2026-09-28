import time

import pytest

from day4_heaps.lru import LRUCache, LRUCacheOD


@pytest.fixture(params=[LRUCacheOD, LRUCache])
def cls(request):
    return request.param


def test_basic_eviction(cls):
    c = cls(2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1  # a is now MRU
    c.put("c", 3)  # evicts b
    assert c.get("b") is None
    assert c.get("b", -1) == -1
    assert c.get("a") == 1 and c.get("c") == 3
    assert len(c) == 2


def test_update_refreshes(cls):
    c = cls(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("a", 10)  # update -> a is MRU
    c.put("c", 3)  # evicts b
    assert c.get("a") == 10
    assert c.get("b") is None
    assert len(c) == 2


def test_capacity_one(cls):
    c = cls(1)
    c.put(1, 1)
    c.put(2, 2)
    assert c.get(1) is None and c.get(2) == 2 and len(c) == 1


def test_falsy_values(cls):
    c = cls(2)
    c.put("z", 0)
    assert c.get("z", "missing") == 0


def test_constant_time(cls):
    c = cls(50_000)
    start = time.perf_counter()
    for i in range(200_000):
        c.put(i, i)
        c.get(i - 10)
    assert time.perf_counter() - start < 3.0
    assert len(c) == 50_000
