from entities.Player import Player


class Storage:
    def __init__(self, asteroids=(), players=(), spacecrafts=(), bullets=()):
        self.asteroids = list(asteroids)
        self.players = list(players)
        self.spacecrafts = list(spacecrafts)
        self.bullets = list(bullets)

    def get_player_by_id(self, player_id) -> Player:
        for player in self.players:
            if player.player_id == player_id:
                return player
        raise Exception(f"Player with id {player_id} not found!")
