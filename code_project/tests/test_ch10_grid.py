from code_project.foundations.ch10_grid import move


def test_move_right():
    assert move((2, 3), 1, 0) == (3, 3)


def test_move_down():
    assert move((2, 3), 0, 1) == (2, 4)
