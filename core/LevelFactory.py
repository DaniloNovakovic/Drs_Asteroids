from persistance.Storage import Storage
from core.utils.Enums import AsteroidSize
from core.utils import asteroid_factory
from Drs_Asteroids.entities.Player import Player
from Drs_Asteroids.entities.Spaceship import Spaceship


class LevelFactory:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def create_new(self, level_number: int = 0) -> Storage:
        asteroids = self._create_new_asteroids(num_asteroids=level_number + 1)
        player = Player(player_id='1', spaceship_id='1')
        ship = Spaceship(400, 200, 2, -45, 1, '1', '1', 'green')
        return Storage(asteroids=asteroids, players=[player], spacecrafts=[ship])

    def _create_new_asteroids(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(num_asteroids):
            # TODO: Randomize x,y for asteroid based on screen_width & screen_height
            asteroids.append(asteroid_factory.create_asteroid(AsteroidSize.medium, x=300, y=300))
        return asteroids
