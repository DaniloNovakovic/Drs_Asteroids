import sys

from PyQt5.QtWidgets import QMainWindow, QApplication


class AsteroidsGame(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(600, 400)
        self.setWindowTitle('Asteroids')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    asteroidsGame = AsteroidsGame()
    asteroidsGame.show()
    sys.exit(app.exec_())
