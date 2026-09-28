"""Day 5 — /proc parsing with pathlib.

/proc/<pid>/status looks like:
    Name:\tpython3
    State:\tS (sleeping)
    Pid:\t1234
    VmRSS:\t   10240 kB
    ...
Kernel threads have no VmRSS line. Processes can vanish between listing
/proc and reading their status file.
"""
from pathlib import Path


def parse_status(text: str) -> dict[str, str]:
    """'Key:\\tvalue' lines -> {key: stripped value}. Ignore lines without ':'."""
    raise NotImplementedError


def top_rss(proc_root: str | Path = "/proc", n: int = 5) -> list[tuple[int, str, int]]:
    """Return up to n (pid, name, rss_kb) tuples, highest RSS first, ties by pid asc.

    Skip: non-numeric entries (e.g. /proc/self, /proc/meminfo), processes without
    VmRSS, and processes whose status can't be read (FileNotFoundError,
    PermissionError, ProcessLookupError — they raced with us).
    """
    raise NotImplementedError


if __name__ == "__main__":
    for pid, name, rss in top_rss():
        print(f"{pid:>7} {rss:>10,} kB  {name}")
