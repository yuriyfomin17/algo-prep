"""Day 5 — regex log parsing.

App log line format:
    2026-10-01T12:00:03.123Z ERROR [feed-handler] seq gap from=100 to=105
    <ISO timestamp>          <LEVEL> [<component>] <message>
LEVEL is one of DEBUG, INFO, WARN, ERROR. Anything else => not a valid line.
"""
import re  # noqa: F401  (you'll want re.compile at module level)
from collections.abc import Iterable


def parse_line(line: str) -> dict | None:
    """Return {'ts', 'level', 'component', 'msg'} (all str, msg stripped) or None."""
    raise NotImplementedError


def extract_kv(msg: str) -> dict[str, int | str]:
    """All key=value tokens in msg. Values made only of digits become int.
    'seq gap from=100 to=105 venue=XNAS' -> {'from': 100, 'to': 105, 'venue': 'XNAS'}"""
    raise NotImplementedError


def errors_per_minute(lines: Iterable[str]) -> dict[str, int]:
    """Count ERROR lines per minute, keyed 'YYYY-MM-DDTHH:MM'. Skip invalid lines."""
    raise NotImplementedError
