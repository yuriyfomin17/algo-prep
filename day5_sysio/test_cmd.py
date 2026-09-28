import sys

from day5_sysio.cmd import run

PY = sys.executable


def test_ok():
    assert run([PY, "-c", "print('hi')"]) == (0, "hi\n", "")


def test_nonzero_exit_and_stderr():
    rc, out, err = run([PY, "-c", "import sys; sys.stderr.write('boom'); sys.exit(3)"])
    assert (rc, out, err) == (3, "", "boom")


def test_timeout():
    assert run([PY, "-c", "import time; time.sleep(5)"], timeout=0.3) == (-1, "", "timeout")


def test_not_found():
    rc, out, err = run(["definitely-not-a-real-binary-xyz"])
    assert rc == 127 and out == "" and err


def test_no_shell_injection():
    rc, out, _ = run(["echo", "$HOME; rm -rf /"])
    assert rc == 0 and out == "$HOME; rm -rf /\n"
