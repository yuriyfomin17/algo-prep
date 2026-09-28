import io

from day2_collections.log_counts import main, status_by_path, top_k_ips

LOG = """\
10.0.0.1 - - [01/Oct/2026:12:00:01 +0000] "GET /api/orders HTTP/1.1" 200 512
10.0.0.2 - - [01/Oct/2026:12:00:02 +0000] "GET /api/orders?id=7 HTTP/1.1" 200 128
10.0.0.1 - - [01/Oct/2026:12:00:03 +0000] "POST /api/orders HTTP/1.1" 500 0

garbage line
10.0.0.3 - - [01/Oct/2026:12:00:04 +0000] "GET /health HTTP/1.1" 200 2
10.0.0.2 - - [01/Oct/2026:12:00:05 +0000] "GET /health HTTP/1.1" 503 0
10.0.0.9 - - [01/Oct/2026:12:00:06 +0000] "GET /health HTTP/1.1" abc 0
10.0.0.1 - - [01/Oct/2026:12:00:07 +0000] "GET /health HTTP/1.1" 200 2
""".splitlines(keepends=True)


def test_top_k_basic():
    assert top_k_ips(LOG, 2) == [("10.0.0.1", 3), ("10.0.0.2", 2)]


def test_top_k_ties_broken_by_ip():
    assert top_k_ips(LOG, 3) == [("10.0.0.1", 3), ("10.0.0.2", 2), ("10.0.0.3", 1)]


def test_top_k_larger_than_distinct():
    assert len(top_k_ips(LOG, 100)) == 3  # 10.0.0.9 line is invalid (status 'abc')


def test_top_k_streams_from_generator():
    gen = (line for line in LOG)
    assert top_k_ips(gen, 1) == [("10.0.0.1", 3)]


def test_top_k_empty():
    assert top_k_ips([], 5) == []


def test_status_by_path():
    got = status_by_path(LOG)
    assert got == {
        "/api/orders": {200: 2, 500: 1},
        "/health": {200: 2, 503: 1},
    }
    assert all(isinstance(v, dict) for v in got.values())


def test_main(monkeypatch, capsys):
    monkeypatch.setattr("sys.stdin", io.StringIO("".join(LOG)))
    main(["2"])
    assert capsys.readouterr().out.splitlines() == ["3 10.0.0.1", "2 10.0.0.2"]
