from code_project.foundations.ch11_dictionaries import total_cost


def test_total_cost_basic():
    assert total_cost(["sword", "potion"], {"sword": 20, "potion": 5}) == 25


def test_total_cost_empty_cart():
    assert total_cost([], {"sword": 20}) == 0
