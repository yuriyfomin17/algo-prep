"""Day 6 — market-data sequence number checks (sets, one pass)."""
from collections.abc import Iterable


def analyse(seqs: Iterable[int]) -> dict:
    """Analyse a feed's sequence numbers in arrival order. Return:

    {
      "gaps": [(lo, hi), ...]   # inclusive ranges between min and max seen that
                                # NEVER arrived, ascending
      "duplicates": [...]       # seqs received more than once, ascending, unique
      "out_of_order": [...]     # seqs whose FIRST arrival came after a higher
                                # seq had already arrived, in arrival order
    }
    Example: [1, 2, 5, 3, 3, 7] ->
      gaps [(4, 4), (6, 6)], duplicates [3], out_of_order [3]
    """
    raise NotImplementedError
