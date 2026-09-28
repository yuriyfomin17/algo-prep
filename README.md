# algo-prep — Jump Trading Python drills (Days 2–6)

Stubs raise `NotImplementedError`; every test fails until you implement it.
Docstrings are the spec. No solutions in this repo.

```bash
source .venv/bin/activate
pytest                      # everything
pytest day3_sliding_window  # one day
pytest -k lru               # one topic
```

| Day | Folder | Exercises | Tools to reach for |
|---|---|---|---|
| 2 | `day2_collections` | `top_k_ips`, `status_by_path`, `main` (stdin CLI) | `Counter`, `defaultdict`, `str.split`, `sys.stdin` |
| 3 | `day3_sliding_window` | `RateLimiter`, `max_events_in_window`, `longest_unique_run`, `min_len_sum_at_least` | `deque`, two pointers |
| 4 | `day4_heaps` | `merge_sorted_streams`, `merge_intervals`, `count_in_range`, `LRUCacheOD`, `LRUCache` | `heapq`, `bisect`, `OrderedDict`, linked list |
| 5 | `day5_sysio` | `parse_status`, `top_rss`, `parse_line`, `extract_kv`, `errors_per_minute`, `run` | `pathlib`, `re`, `subprocess` |
| 6 | `day6_graphs` | `analyse` (seq gaps), `descendants`, `kill_order`, `startup_order`, `simplify_path` | sets, iterative DFS/BFS, Kahn + `heapq`, stack |

Manual runs:
```bash
python -m day2_collections.log_counts 5 < data/access.log
python -m day5_sysio.procfs          # real /proc — run inside the jump-lab container
```

Rules (interview conditions):
- Turn off AI/autocomplete in PyCharm for these files.
- Timebox 20–25 min per function; say complexity out loud before running tests.
- After it passes, rewrite it once more from scratch without looking (Day 9).
