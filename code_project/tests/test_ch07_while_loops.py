from code_project.foundations.ch07_while_loops import countdown


def test_countdown_basic():
    assert countdown(3) == [3, 2, 1]


def test_countdown_zero_gives_empty_list():
    assert countdown(0) == []
