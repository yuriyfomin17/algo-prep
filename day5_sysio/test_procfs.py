from day5_sysio.procfs import parse_status, top_rss


def status(name, pid, rss_kb=None):
    lines = [f"Name:\t{name}", "State:\tS (sleeping)", f"Pid:\t{pid}"]
    if rss_kb is not None:
        lines.append(f"VmRSS:\t{rss_kb:>8} kB")
    lines.append("Threads:\t1")
    return "\n".join(lines) + "\n"


def make_proc(tmp_path, procs):
    for pid, name, rss in procs:
        d = tmp_path / str(pid)
        d.mkdir()
        (d / "status").write_text(status(name, pid, rss))
    return tmp_path


def test_parse_status():
    s = parse_status(status("feedhandler", 42, 2048) + "no colon here\n")
    assert s["Name"] == "feedhandler"
    assert s["Pid"] == "42"
    assert s["VmRSS"] == "2048 kB"
    assert s["State"] == "S (sleeping)"


def test_top_rss(tmp_path):
    root = make_proc(
        tmp_path,
        [(1, "systemd", 9000), (200, "kthreadd", None), (300, "java", 500000),
         (301, "python3", 20000), (302, "bash", 3000), (303, "sshd", 20000)],
    )
    (root / "self").mkdir()  # non-numeric
    (root / "meminfo").write_text("MemTotal: 1 kB\n")
    (root / "999").mkdir()  # vanished: dir without status
    assert top_rss(root, 3) == [(300, "java", 500000), (301, "python3", 20000), (303, "sshd", 20000)]
    assert len(top_rss(root, 50)) == 5


def test_top_rss_empty(tmp_path):
    assert top_rss(tmp_path) == []
