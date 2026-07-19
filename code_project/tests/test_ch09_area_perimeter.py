from code_project.foundations.ch09_area_perimeter import perimeter


def test_perimeter_basic():
    assert perimeter(6, 4) == 20


def test_perimeter_square():
    assert perimeter(5, 5) == 20
