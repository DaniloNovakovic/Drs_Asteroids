import sys
from core.Game import Game
from core.Screen import Screen
from core.LevelFactory import LevelFactory
from core.KeyHandler import KeyHandler
from core.MovementHandler import MovementHandler
from core.CollisionHandler import CollisionHandler
from PyQt5.QtWidgets import QApplication


class AsteroidsGame:
    def __init__(self):
        screen_width = 600
        screen_height = 400
        self.screen = Screen(screen_width, screen_height, "Asteroids")

        '''Dependency injection - here you can inject handlers/services into constructor'''

        level_factory = LevelFactory(screen_width=screen_width, screen_height=screen_height)
        key_handler = KeyHandler()
        movement_handler = MovementHandler()
        collision_handler = CollisionHandler(screen_width=screen_width, screen_height=screen_height)

        self.game = Game(self.screen, level_factory=level_factory, key_handler=key_handler,
                         movement_handler=movement_handler, collision_handler=collision_handler)

    def start(self):
        self.screen.show()
        self.game.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    asteroidsGame = AsteroidsGame()
    asteroidsGame.start()
    sys.exit(app.exec_())
