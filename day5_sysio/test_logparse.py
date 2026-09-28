from day5_sysio.logparse import errors_per_minute, extract_kv, parse_line

LINES = [
    "2026-10-01T12:00:03.123Z ERROR [feed-handler] seq gap from=100 to=105\n",
    "2026-10-01T12:00:04.000Z INFO [order-gw] connected venue=XNAS\n",
    "2026-10-01T12:00:59.999Z ERROR [feed-handler] seq gap from=200 to=201\n",
    "2026-10-01T12:01:00.001Z ERROR [risk] limit breached acct=77\n",
    "not a log line\n",
    "2026-10-01T12:01:02.000Z FATAL [risk] bogus level\n",
]


def test_parse_line():
    assert parse_line(LINES[0]) == {
        "ts": "2026-10-01T12:00:03.123Z",
        "level": "ERROR",
        "component": "feed-handler",
        "msg": "seq gap from=100 to=105",
    }
    assert parse_line(LINES[4]) is None
    assert parse_line(LINES[5]) is None
    assert parse_line("") is None


def test_extract_kv():
    assert extract_kv("seq gap from=100 to=105 venue=XNAS") == {"from": 100, "to": 105, "venue": "XNAS"}
    assert extract_kv("nothing here") == {}


def test_errors_per_minute():
    assert errors_per_minute(LINES) == {"2026-10-01T12:00": 2, "2026-10-01T12:01": 1}
