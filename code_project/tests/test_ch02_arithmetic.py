from code_project.foundations.ch02_arithmetic import split_into_teams


def test_split_into_teams_full_teams():
    assert split_into_teams(17, 5) == (3, 2)


def test_split_into_teams_no_leftover():
    assert split_into_teams(20, 5) == (4, 0)
