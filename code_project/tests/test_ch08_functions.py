from code_project.foundations.ch08_functions import area


def test_area_basic():
    assert area(4, 5) == 20


def test_area_zero_width():
    assert area(4, 0) == 0
