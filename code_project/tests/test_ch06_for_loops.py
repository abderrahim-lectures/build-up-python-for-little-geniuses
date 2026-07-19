from code_project.foundations.ch06_for_loops import repeated_addition


def test_repeated_addition_basic():
    assert repeated_addition(3, 4) == 12


def test_repeated_addition_zero_times():
    assert repeated_addition(5, 0) == 0
