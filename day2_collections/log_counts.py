"""Day 2 — collections (Counter, defaultdict) + streaming input.

Log format (combined-log style, whitespace separated):
    <ip> - - [<date> <tz>] "<METHOD> <path> <proto>" <status> <bytes>
e.g.
    10.0.0.1 - - [01/Oct/2026:12:00:01 +0000] "GET /api/orders HTTP/1.1" 200 512

A line is VALID iff it splits into at least 10 whitespace-separated fields and
the 9th field (the status) is an integer. Skip invalid lines — never crash.

Run manually:
    python -m day2_collections.log_counts 3 < data/access.log
"""
from collections.abc import Iterable


def top_k_ips(lines: Iterable[str], k: int) -> list[tuple[str, int]]:
    """Return the k most frequent client IPs as (ip, count), highest count first.

    Ties: IP ascending (plain string comparison).
    Must stream: `lines` may be a file bigger than RAM — don't list() it.
    """
    raise NotImplementedError


def status_by_path(lines: Iterable[str]) -> dict[str, dict[int, int]]:
    """Return path -> {status: count}.

    Query strings are stripped: '/api/x?id=1' counts as '/api/x'.
    """
    raise NotImplementedError


def main(argv: list[str] | None = None) -> None:
    """CLI: read the log from stdin, print top-k as '<count> <ip>' lines.

    k is argv[0] (default 10). argv defaults to sys.argv[1:].
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
