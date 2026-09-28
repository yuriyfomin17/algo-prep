import pytest

from day6_graphs.paths import simplify_path


@pytest.mark.parametrize(
    "path, want",
    [
        ("/a/./b/../../c/", "/c"),
        ("/home//user/", "/home/user"),
        ("/../", "/"),
        ("/", "/"),
        ("/a/b/c/../..", "/a"),
        ("/.../x", "/.../x"),
    ],
)
def test_simplify_path(path, want):
    assert simplify_path(path) == want
