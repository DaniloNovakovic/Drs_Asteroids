import sys
from core.Game import Game
from core.Screen import Screen
from core.LevelFactory import LevelFactory
from core.KeyHandler import KeyHandler
from core.MovementHandler import MovementHandler
from core.CollisionHandler import CollisionHandler
from PyQt5.QtWidgets import QApplication
from datetime import datetime

from core.utils.asteroid_factory import AsteroidFactory
from core.utils.bullet_factory import BulletFactory
from core.utils.spaceship_factory import SpaceshipFactory
from core.utils.heart_factory import HeartFactory

class AsteroidsGame:
    def __init__(self):
        screen_width = 1000
        screen_height = 600
        self.screen = Screen(screen_width, screen_height, "Asteroids")

        '''Dependency injection - here you can inject handlers/services into constructor'''

        spaceship_factory = SpaceshipFactory(screen=self.screen)
        asteroid_factory = AsteroidFactory(screen=self.screen)
        hearts_factory = HeartFactory(screen=self.screen)
        level_factory = LevelFactory(screen_width=screen_width, screen_height=screen_height,
                                     asteroid_factory=asteroid_factory,
                                     spaceship_factory=spaceship_factory,
                                     heart_factory=hearts_factory)
        bullet_factory = BulletFactory(screen=self.screen)
        key_handler = KeyHandler(bullet_factory=bullet_factory)
        movement_handler = MovementHandler(datetime.now(), screen_width, screen_height)
        collision_handler = CollisionHandler(screen_width=screen_width, screen_height=screen_height)

        self.game = Game(self.screen, level_factory=level_factory, key_handler=key_handler,
                         collision_handler=collision_handler, movement_handler=movement_handler)

    def start(self):
        self.screen.show()
        self.game.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    asteroidsGame = AsteroidsGame()
    asteroidsGame.start()
    sys.exit(app.exec_())
