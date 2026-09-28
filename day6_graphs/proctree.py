"""Day 6 — process tree (iterative DFS/BFS; no recursion — trees can be deep).

rows are (pid, ppid, cmd) tuples, like `ps -eo pid,ppid,comm`.
"""


def descendants(rows: list[tuple[int, int, str]], root: int) -> list[int]:
    """All descendant pids of root (not root itself), ascending."""
    raise NotImplementedError


def kill_order(rows: list[tuple[int, int, str]], root: int) -> list[int]:
    """root and all its descendants, ordered so every child comes before its parent
    (so killing in this order never orphans a live process). root is last."""
    raise NotImplementedError
