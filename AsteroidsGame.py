import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication

from core.CollisionHandler import CollisionHandler
from core.Game import Game
from core.KeyHandler import KeyHandler
from core.LevelFactory import LevelFactory
from core.MovementHandler import MovementHandler
from core.Screen import Screen
from core.utils.asteroid_factory import AsteroidFactory
from core.utils.bullet_factory import BulletFactory
from core.utils.heart_factory import HeartFactory
from core.utils.player_factory import PlayerFactory
from core.utils.spaceship_factory import SpaceshipFactory
from entities.PlayerInput import PlayerInput


class AsteroidsGame:
    def __init__(self, player_inputs=[], screen_width=1000, screen_height=600):
        self.screen = Screen(screen_width, screen_height, "Asteroids")

        '''Dependency injection - here you can inject handlers/services into constructor'''

        spaceship_factory = SpaceshipFactory(screen=self.screen)
        asteroid_factory = AsteroidFactory(screen=self.screen)
        hearts_factory = HeartFactory(screen=self.screen)
        player_factory = PlayerFactory(screen=self.screen)
        level_factory = LevelFactory(screen_width=screen_width, screen_height=screen_height,
                                     asteroid_factory=asteroid_factory,
                                     spaceship_factory=spaceship_factory,
                                     heart_factory=hearts_factory,
                                     player_factory=player_factory,
                                     player_inputs=player_inputs)
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
    asteroidsGame = AsteroidsGame(player_inputs=[PlayerInput(player_id="djura", color="red"),
                                                 PlayerInput(player_id="steva", color="yellow")])
    asteroidsGame.start()
    sys.exit(app.exec_())
