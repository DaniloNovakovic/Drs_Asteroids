import sys

from PyQt5.QtWidgets import QApplication
from AsteroidsGame import AsteroidsGame

if __name__ == "__main__":
    app = QApplication(sys.argv)
    asteroidsGame = AsteroidsGame()
    asteroidsGame.start()
    sys.exit(app.exec_())
