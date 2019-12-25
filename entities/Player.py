from entities.PlayerConfig import PlayerConfig


class Player:
    def __init__(self, player_id: str, spaceship_id: str, player_config: PlayerConfig = None, num_points: int = 0, num_lives: int = 3):
        self.player_id = player_id
        self.spaceship_id = spaceship_id
        self.num_points = num_points
        self.num_lives = num_lives
        self.player_config = player_config

    def remove_life(self):
        self.num_lives -= 1

    def increase_points(self, num_points_to_add: int):
        self.num_points += num_points_to_add

    def is_dead(self) -> bool:
        return self.num_lives <= 0
