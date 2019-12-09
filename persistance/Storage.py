from entities import Asteroid, Bullet, Player, Spaceship


class Storage:
    def __init__(self, asteroids=(), players=(), spacecrafts=(), bullets=()):
        self.asteroids = list(asteroids)
        self.players = list(players)
        self.spacecrafts = list(spacecrafts)
        self.bullets = list(bullets)

    '''Getters for all objects on screen'''

    def get_all_asteroids(self):
        return self.asteroids

    def get_all_spacecrafts(self):
        return self.spacecrafts

    '''Getters for single objects on screen'''

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

    '''Object generators'''

    def add_bullet(self, bullet: Bullet):
        self.bullets.append(bullet)

    def add_asteroid(self, asteroid: Asteroid):
        self.asteroids.append(asteroid)
