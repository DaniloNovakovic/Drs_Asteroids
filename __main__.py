import sys
from Display.Game import Game
from Display.Screen import Screen
from PyQt5.QtWidgets import QApplication


class AsteroidsGame:
    def __init__(self):
        self.screen = Screen(600, 400, "Asteroids")
        self.game = Game(self.screen)

    def start(self):
        self.screen.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    asteroidsGame = AsteroidsGame()
    asteroidsGame.start()
    sys.exit(app.exec_())
