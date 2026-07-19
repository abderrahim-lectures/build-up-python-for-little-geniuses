from code_project.foundations.ch04_conditionals import health_status


def test_health_status_defeated():
    assert health_status(0) == "defeated"


def test_health_status_low():
    assert health_status(24) == "low health"


def test_health_status_ok_at_boundary():
    assert health_status(25) == "ok"
