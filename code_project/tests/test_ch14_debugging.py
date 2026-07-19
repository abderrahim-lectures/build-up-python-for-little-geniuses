from code_project.foundations.ch14_debugging import safe_divide


def test_safe_divide_normal():
    assert safe_divide(10, 2) == 5


def test_safe_divide_by_zero_returns_none():
    assert safe_divide(10, 0) is None
