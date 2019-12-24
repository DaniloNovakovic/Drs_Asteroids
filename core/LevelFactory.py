from random import randint

from core.utils.spaceship_factory import SpaceshipFactory
from core.utils.asteroid_factory import AsteroidFactory
from entities.Player import Player
from persistance.Storage import Storage


class LevelFactory:
    def __init__(self, screen_width, screen_height, asteroid_factory: AsteroidFactory,
                 spaceship_factory: SpaceshipFactory):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.asteroid_factory = asteroid_factory
        self.spaceship_factory = spaceship_factory

    def create_new(self, level_number: int = 0) -> Storage:
        asteroids = self._create_new_asteroids(num_asteroids=level_number + 5)
        players = self._create_new_players()
        spaceships = self._create_new_spaceships()
        return Storage(asteroids=asteroids, players=players, spacecrafts=spaceships)

    def _create_new_asteroids(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(num_asteroids):
            # TODO: Randomize x,y and velocity for asteroid based on screen_width & screen_height so that they come
            #  from the outside of screen towards center
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = 0 # randint(asteroid.r, self.screen_width - asteroid.r)
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.1
            asteroids.append(asteroid)
        return asteroids

    def _create_new_players(self) -> list:
        player1 = Player(player_id='1', spaceship_id='1')
        player2 = Player(player_id='2', spaceship_id='2')
        player3 = Player('3', '3')
        player4 = Player('4', '4')
        return [player1, player2, player3, player4]

    def _create_new_spaceships(self):
        ship1 = self.spaceship_factory.create_spaceship('1', '1', 'red', x=(self.screen_width / 2 - 50),
                                                        y=(self.screen_height / 2), angle=-180)
        ship2 = self.spaceship_factory.create_spaceship('2', '2', 'yellow', x=(self.screen_width / 2 + 50),
                                                        y=(self.screen_height / 2), angle=-180)
        # ship3 = spaceship_factory.create_spaceship('3', '3', 'blue', x=100, y=250, velocity=10)
        # ship4 = spaceship_factory.create_spaceship('4', '4', 'green', x=300, y=250, velocity=20)
        return [ship1, ship2]
