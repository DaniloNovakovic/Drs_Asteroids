from persistance.Storage import Storage
from core.utils.Enums import AsteroidSize
from core.utils import asteroid_factory
from Drs_Asteroids.entities.Player import Player
from Drs_Asteroids.entities.Spaceship import Spaceship
from random import randint

class LevelFactory:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def create_new(self, level_number: int = 0) -> Storage:
        asteroids = self._create_new_asteroids(num_asteroids=level_number + 1)
        player = Player(player_id='1', spaceship_id='1')
        ship = Spaceship(200, 200, 2, -45, 1, '1', '1', 'green')
        return Storage(asteroids=asteroids, players=[player], spacecrafts=[ship])

    def _create_new_asteroids(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(num_asteroids):
            # TODO: Randomize x,y for asteroid based on screen_width & screen_height
            asteroid = asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = randint(asteroid.r, self.screen_width - asteroid.r)
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroids.append(asteroid)
        return asteroids
