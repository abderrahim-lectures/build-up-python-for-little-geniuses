from code_project.build_game.world import World


def test_new_world_spawns_player_at_center():
    world = World(player_name="Ada", grid_width=10, grid_height=10)
    assert world.spawn_point() == (5, 5)


def test_new_world_remembers_player_name():
    world = World(player_name="Ada")
    assert world.player_name == "Ada"
