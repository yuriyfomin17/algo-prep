from day6_graphs.proctree import descendants, kill_order

ROWS = [
    (1, 0, "systemd"),
    (100, 1, "sshd"),
    (200, 100, "bash"),
    (201, 200, "python3"),
    (202, 200, "tail"),
    (300, 201, "worker"),
    (400, 1, "cron"),
]


def test_descendants():
    assert descendants(ROWS, 100) == [200, 201, 202, 300]
    assert descendants(ROWS, 202) == []
    assert descendants(ROWS, 1) == [100, 200, 201, 202, 300, 400]


def test_kill_order():
    order = kill_order(ROWS, 100)
    assert sorted(order) == [100, 200, 201, 202, 300]
    assert order[-1] == 100
    pos = {pid: i for i, pid in enumerate(order)}
    parent = {pid: ppid for pid, ppid, _ in ROWS}
    for pid in order[:-1]:
        assert pos[pid] < pos[parent[pid]]


def test_deep_chain_no_recursion_limit():
    rows = [(i, i - 1, "x") for i in range(1, 20_001)]
    assert len(descendants(rows, 0)) == 20_000
    order = kill_order(rows, 0)
    assert order[0] == 20_000 and order[-1] == 0
