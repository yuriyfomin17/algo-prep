import pytest

from day6_graphs.deps import startup_order


def test_order():
    deps = {
        "strategy": ["md-feed", "order-gw", "risk"],
        "order-gw": ["risk"],
        "md-feed": ["ptp"],
        "risk": [],
    }
    assert startup_order(deps) == ["ptp", "md-feed", "risk", "order-gw", "strategy"]


def test_independent_services_alphabetical():
    assert startup_order({"c": [], "a": [], "b": []}) == ["a", "b", "c"]


def test_empty():
    assert startup_order({}) == []


def test_cycle():
    with pytest.raises(ValueError):
        startup_order({"a": ["b"], "b": ["c"], "c": ["a"]})
