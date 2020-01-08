from random import randint

from PyQt5.Qt import Qt

from core.utils.asteroid_factory import AsteroidFactory
from core.utils.heart_factory import HeartFactory
from core.utils.player_factory import PlayerFactory
from core.utils.spaceship_factory import SpaceshipFactory
from entities.PlayerConfig import PlayerConfig
from entities.PlayerInput import PlayerInput
from persistance.Storage import Storage


class LevelFactory:
    def __init__(self, screen_width, screen_height, asteroid_factory: AsteroidFactory,
                 spaceship_factory: SpaceshipFactory, heart_factory: HeartFactory,
                 player_factory: PlayerFactory, player_inputs=None):
        if player_inputs is None:
            player_inputs = [PlayerInput(player_id="1", color="red")]

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.asteroid_factory = asteroid_factory
        self.spaceship_factory = spaceship_factory
        self.heart_factory = heart_factory
        self.player_factory = player_factory
        self.player_inputs = player_inputs

    def create_new(self, level_number: int = 1, prev_storage: Storage = None) -> Storage:
        asteroids = []

        players = self._create_new_players() if prev_storage is None else prev_storage.players
        spaceships = self._create_new_spaceships()
        hearts = self._create_new_hearts()

        if level_number == 1:
            asteroids = self._create_new_asteroids(num_asteroids=level_number + 5)
        elif level_number == 2:
            asteroids = self._create_new_asteroids2(num_asteroids=level_number + 6)
        elif level_number == 3:
            asteroids = self._create_new_asteroids3(num_asteroids=level_number + 6)
        elif level_number == 4:
            asteroids = self._create_new_asteroids4(num_asteroids=level_number + 8)
        elif level_number == 5:
            asteroids = self._create_new_asteroids5(num_asteroids=level_number + 7)
        else:
            #trigeruje se event
            pass

        return Storage(asteroids=asteroids, players=players, spacecrafts=spaceships, hearts=hearts)

    def _create_new_players(self) -> list:
        """
        Creates new players based on self.player_inputs.
        Note: Current implementation only supports 1 or 2 players.
        """
        players = []
        index = 0
        for player_input in self.player_inputs:
            config = PlayerConfig(bullet_color=player_input.color)
            if index > 0:
                config = PlayerConfig(key_left=Qt.Key_A, key_right=Qt.Key_D, key_down=Qt.Key_S
                                      , key_up=Qt.Key_W, key_shoot=Qt.Key_Control, bullet_color=player_input.color)
            player = self.player_factory.create_player(player_id=player_input.player_id,
                                                       spaceship_id=player_input.player_id, player_config=config,
                                                       status_x=0, status_y=index*15)
            players.append(player)
            index += 1
        return players

    def _create_new_spaceships(self):
        spaceships = []
        index = 0
        for player_input in self.player_inputs:
            x = (self.screen_width / 2 - 50)
            y = (self.screen_height / 2)
            if index > 0:
                x = (self.screen_width / 2 + 50)
            ship = self.spaceship_factory.create_spaceship(spaceship_id=player_input.player_id,
                                                           player_id=player_input.player_id,
                                                           color=player_input.color,
                                                           x=x, y=y, angle=-180)
            spaceships.append(ship)
            index += 1
        return spaceships

    def _create_new_hearts(self):  # srca koja mogu da se pokupe
        heart1 = self.heart_factory.create_heart('1', x=150 + randint(-100, 100), y=150 + randint(-100, 100))
        heart2 = self.heart_factory.create_heart('2', x=300 + randint(-100, 100), y=300 + randint(-100, 100))
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
