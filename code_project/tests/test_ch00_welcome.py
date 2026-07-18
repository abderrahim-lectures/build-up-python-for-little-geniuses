from code_project.foundations.ch00_welcome import greet


def test_greet_includes_name():
    assert "Ada" in greet("Ada")


def test_greet_is_friendly():
    message = greet("Little Genius")
    assert message.startswith("Welcome")
