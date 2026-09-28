"""Day 6 — service startup order (topological sort, Kahn's algorithm + heapq)."""


def startup_order(deps: dict[str, list[str]]) -> list[str]:
    """deps[svc] = services that must be started BEFORE svc.

    Services that appear only as dependencies are included too.
    Deterministic: whenever several services are ready, start the alphabetically
    smallest first. Raise ValueError on a cycle.
    """
    raise NotImplementedError
