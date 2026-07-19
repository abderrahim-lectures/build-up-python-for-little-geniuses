from code_project.foundations.ch03_strings import player_status


def test_player_status_includes_name():
    assert "Ari" in player_status("Ari", 10)


def test_player_status_includes_score():
    assert "10" in player_status("Ari", 10)
