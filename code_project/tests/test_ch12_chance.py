from code_project.foundations.ch12_chance import roll_die


def test_roll_die_default_in_range():
    assert 1 <= roll_die() <= 6


def test_roll_die_custom_sides_in_range():
    assert 1 <= roll_die(20) <= 20
