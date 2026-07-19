from code_project.foundations.ch05_lists import add_item


def test_add_item_appends():
    assert add_item(["sword"], "potion") == ["sword", "potion"]


def test_add_item_grows_length_by_one():
    assert len(add_item(["sword", "shield"], "potion")) == 3
