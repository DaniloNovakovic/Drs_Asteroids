import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox

# from AsteroidsGame import AsteroidsGame
from core.utils.image_helper import get_full_image_path


# from entities.PlayerInput import PlayerInput


class Score(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("Scores")
        self.initUI()

    def initUI(self):
        self.initWindow()

    def read_from_file(self):
        f = open("test.txt", "r")
        print(f.readline())

    def initWindow(self):
        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)


def wi():
    app = QApplication(sys.argv)
    win = Score()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    wi()
