"""Day 5 — running commands safely with subprocess."""


def run(args: list[str], timeout: float = 5.0) -> tuple[int, str, str]:
    """Run a command WITHOUT a shell and return (returncode, stdout, stderr) as text.

    - timeout expired      -> (-1, "", "timeout")
    - executable not found -> (127, "", <error message>)
    Never raise for a non-zero exit code.
    """
    raise NotImplementedError
