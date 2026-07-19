from code_project.foundations.ch01_variables import describe_player


def test_describe_player_includes_name():
    assert "Ari" in describe_player("Ari", 0, 100)


def test_describe_player_includes_score_and_health():
    assert "score: 10" in describe_player("Ari", 10, 50) and "health: 50" in describe_player("Ari", 10, 50)
