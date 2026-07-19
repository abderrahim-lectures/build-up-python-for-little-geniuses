from code_project.foundations.ch15_capstone import build_summary


def test_build_summary_includes_name():
    assert "Ari" in build_summary("Ari", ["sword"], {"potion": 5})


def test_build_summary_includes_item():
    assert "sword" in build_summary("Ari", ["sword"], {"potion": 5})
