from code_project.foundations.ch13_classes import Player


def test_player_init_sets_attributes():
    hero = Player("Ari", 100)
    assert hero.name == "Ari" and hero.health == 100


def test_player_take_damage_reduces_health():
    hero = Player("Ari", 100)
    hero.take_damage(30)
    assert hero.health == 70


def test_player_health_never_negative():
    hero = Player("Ari", 10)
    hero.take_damage(999)
    assert hero.health == 0
