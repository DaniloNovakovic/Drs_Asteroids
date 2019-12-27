from random import randint

from core.utils.heart_factory import HeartFactory
from core.utils.spaceship_factory import SpaceshipFactory
from core.utils.asteroid_factory import AsteroidFactory
from entities.Player import Player
from persistance.Storage import Storage
from entities.PlayerConfig import PlayerConfig
from PyQt5.Qt import Qt


class LevelFactory:
    def __init__(self, screen_width, screen_height, asteroid_factory: AsteroidFactory,
                 spaceship_factory: SpaceshipFactory, heart_factory: HeartFactory):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.asteroid_factory = asteroid_factory
        self.spaceship_factory = spaceship_factory
        self.heart_factory = heart_factory

    def create_new(self, level_number: int = 1, storage: Storage = None) -> Storage:
        if level_number == 1:
            asteroids = self._create_new_asteroids(num_asteroids=level_number + 5)
            players = self._create_new_players()
            spaceships = self._create_new_spaceships()
            hearts = self._create_new_hearts()
            return Storage(asteroids=asteroids, players=players, spacecrafts=spaceships, hearts=hearts)
        elif level_number == 2:
            asteroids = self._create_new_asteroids2(num_asteroids=level_number + 6)
            players = self._create_new_players()
            spaceships = self._create_new_spaceships()
            hearts = self._create_new_hearts()
            return Storage(asteroids=asteroids, players=players, spacecrafts=spaceships, hearts=hearts)
        elif level_number == 3:
            asteroids = self._create_new_asteroids3(num_asteroids=level_number + 6)
            players = self._create_new_players()
            spaceships = self._create_new_spaceships()
            hearts = self._create_new_hearts()
            return Storage(asteroids=asteroids, players=players, spacecrafts=spaceships, hearts=hearts)
        elif level_number == 4:
            asteroids = self._create_new_asteroids4(num_asteroids=level_number + 8)
            players = self._create_new_players()
            spaceships = self._create_new_spaceships()
            hearts = self._create_new_hearts()
            return Storage(asteroids=asteroids, players=players, spacecrafts=spaceships, hearts=hearts)
        elif level_number == 5:
            asteroids = self._create_new_asteroids5(num_asteroids=level_number + 7)
            players = self._create_new_players()
            spaceships = self._create_new_spaceships()
            hearts = self._create_new_hearts()
            return Storage(asteroids=asteroids, players=players, spacecrafts=spaceships, hearts=hearts)

    def _create_new_players(self) -> list:
        player1_config = PlayerConfig()
        player1 = Player(player_id='1', spaceship_id='1', player_config=player1_config)
        player2_config = PlayerConfig(key_left=Qt.Key_A, key_right=Qt.Key_D, key_down=Qt.Key_S
                                      , key_up=Qt.Key_W, key_shoot=Qt.Key_Control)
        player2 = Player(player_id='2', spaceship_id='2', player_config=player2_config)
        # player3 = Player('3', '3')
        # player4 = Player('4', '4')
        return [player1, player2]

    def _create_new_spaceships(self):
        ship1 = self.spaceship_factory.create_spaceship('1', '1', 'red', x=(self.screen_width / 2 - 50),
                                                        y=(self.screen_height / 2), angle=-180)
        ship2 = self.spaceship_factory.create_spaceship('2', '2', 'yellow', x=(self.screen_width / 2 + 50),
                                                        y=(self.screen_height / 2), angle=-180)
        # ship3 = spaceship_factory.create_spaceship('3', '3', 'blue', x=100, y=250, velocity=10)
        # ship4 = spaceship_factory.create_spaceship('4', '4', 'green', x=300, y=250, velocity=20)
        return [ship1, ship2]

    def _create_new_hearts(self):
        heart1 = self.heart_factory.create_heart('1', x=0, y=self.screen_height)
        heart2 = self.heart_factory.create_heart('2', x=(self.screen_width-50), y=self.screen_height)
        return [heart1, heart2]

    def _create_new_asteroids(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(num_asteroids):
            # TODO: Randomize x,y and velocity for asteroid based on screen_width & screen_height so that they come
            #  from the outside of screen towards center
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = 0  # randint(asteroid.r, self.screen_width - asteroid.r)
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.1
            asteroids.append(asteroid)
        return asteroids

    def _create_new_asteroids2(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(0, 4):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = 0
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.15
            asteroids.append(asteroid)
        for _ in range(4, 8):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = self.screen_width
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.15
            asteroid.angle = 180
            asteroids.append(asteroid)
        return asteroids

    def _create_new_asteroids3(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(0, 3):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = 0
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.2
            asteroids.append(asteroid)
        for _ in range(3, 6):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = self.screen_width
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.2
            asteroid.angle = 180
            asteroids.append(asteroid)
        for i in range(6, 9):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = ((self.screen_width / 2) - 100) + (i * 150)
            asteroid.y = 0
            asteroid.velocity = 0.2
            asteroid.angle = 90
            asteroids.append(asteroid)
        return asteroids

    def _create_new_asteroids4(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(0, 3):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = 0
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.25
            asteroids.append(asteroid)
        for _ in range(3, 6):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = self.screen_width
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.25
            asteroid.angle = 180
            asteroids.append(asteroid)
        for i in range(6, 9):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = ((self.screen_width / 2) - 100) + (i * 150)
            asteroid.y = 0
            asteroid.velocity = 0.25
            asteroid.angle = 90
            asteroids.append(asteroid)
        for i in range(9, 12):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = ((self.screen_width / 2) - 500) + (i * 150)
            asteroid.y = 0
            asteroid.velocity = 0.25
            asteroid.angle = 270
            asteroids.append(asteroid)
        return asteroids

    def _create_new_asteroids5(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(0, 3):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = 0
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.3
            asteroids.append(asteroid)
        for _ in range(3, 6):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = self.screen_width
            asteroid.y = randint(asteroid.r, self.screen_height - asteroid.r)
            asteroid.velocity = 0.3
            asteroid.angle = 180
            asteroids.append(asteroid)
        for i in range(6, 9):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = ((self.screen_width / 2) - 100) + (i * 150)
            asteroid.y = 0
            asteroid.velocity = 0.3
            asteroid.angle = 90
            asteroids.append(asteroid)
        for i in range(9, 12):
            asteroid = self.asteroid_factory.create_asteroid(asteroid_type=randint(0, 2))
            asteroid.x = ((self.screen_width / 2) - 500) + (i * 150)
            asteroid.y = 0
            asteroid.velocity = 0.3
            asteroid.angle = 270
            asteroids.append(asteroid)
        return asteroids
