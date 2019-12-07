from entities.Player import Player
from entities.Spaceship import Spaceship
from entities.Bullet import Bullet


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

    def get_first_player_id(self) -> Player:
        for player in self.players:
            return player.player_id

    def get_spaceship_by_player_id(self, player_id) -> Spaceship:
        for spaceship in self.spacecrafts:
            if spaceship.player_id == player_id:
                return spaceship
        raise Exception(f"Spaceship with player id {player_id} not found!")

    def add_bullet(self, bullet: Bullet):
        self.bullets.append(bullet)
