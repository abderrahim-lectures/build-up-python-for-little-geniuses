"""Chapter 2: Arithmetic. Order of operations isn't just a math-class rule – Python follows it exactly, so knowing it tells you exactly what your code will compute."""


def split_into_teams(players: int, team_size: int):
    """Return (full_teams, leftover_players) for splitting players into teams."""
    return players // team_size, players % team_size
