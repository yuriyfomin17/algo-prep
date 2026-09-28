from day6_graphs.seqgaps import analyse


def test_docstring_example():
    assert analyse([1, 2, 5, 3, 3, 7]) == {
        "gaps": [(4, 4), (6, 6)],
        "duplicates": [3],
        "out_of_order": [3],
    }


def test_clean_feed():
    assert analyse(range(100, 200)) == {"gaps": [], "duplicates": [], "out_of_order": []}


def test_empty():
    assert analyse([]) == {"gaps": [], "duplicates": [], "out_of_order": []}


def test_big_gap_and_late_fill():
    got = analyse([10, 11, 20, 12, 13, 21, 21, 10])
    assert got["gaps"] == [(14, 19)]
    assert got["duplicates"] == [10, 21]
    assert got["out_of_order"] == [12, 13]


def test_generator_input():
    assert analyse(x for x in [3, 1])["out_of_order"] == [1]
