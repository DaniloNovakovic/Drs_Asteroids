import sys
from AsteroidsGame import AsteroidsGame
from entities.PlayerInput import PlayerInput

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox

from core.utils.image_helper import get_full_image_path


class SinglePlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("OnePlayer")
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.username()
        self.chooseShip()
        self.buttonPlay()

    def initWindow(self):
        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def username(self):
        self.enterNameLabel = QtWidgets.QLabel(self)
        self.enterNameLabel.setText("Enter name")
        self.enterNameLabel.setGeometry(200, 150, 200, 50)
        self.enterNameLabel.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        self.player1NameLineEdit = QLineEdit(self)
        self.player1NameLineEdit.setGeometry(200, 200, 200, 50)

    def chooseShip(self):
        self.choseShipLabel = QLabel(self)
        self.choseShipLabel.setText("Choose ship")
        self.choseShipLabel.setGeometry(410, 150, 200, 50)
        self.choseShipLabel.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        self.player1Cb = QComboBox(self)
        # self.player1Cb.setCursor(Qt.PointingHandCursor)
        self.player1Cb.setStyleSheet("border:1px solid rgb(220, 20, 60); color: red; font-family: Helvetica;");
        self.player1Cb.addItem("")
        self.player1Cb.addItem("red")
        self.player1Cb.addItem("green")
        self.player1Cb.addItem("yellow")
        self.player1Cb.addItem("blue")

        self.player1Cb.model().item(0).setEnabled(False)
        self.player1Cb.setGeometry(410, 200, 200, 50)

    def buttonPlay(self):
        self.playButton = QtWidgets.QPushButton(self)
        self.playButton.setText("PLAY")
        self.playButton.setGeometry(750, 400, 200, 50)
        self.playButton.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;")
        self.playButton.clicked.connect(self.onPlayButtonClicked)

    def onPlayButtonClicked(self):
        player1_input = PlayerInput(player_id=self.player1NameLineEdit.text(), color=self.player1Cb.currentText())

        # TODO: Fix crash
        # self.game = AsteroidsGame(player_inputs=[player1_input])
        # self.game.start()

def wi():
    app = QApplication(sys.argv)
    win = SinglePlayerWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    wi()
