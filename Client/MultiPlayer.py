from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox
import sys
from core.utils.image_helper import get_full_image_path


class MultiPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("MultiPlayer")
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.username()
        self.chooseShip()
        self.labels()
        self.buttonPlay()

    def initWindow(self):
        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def username(self):
        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Enter name")
        self.lbl2.setGeometry(200, 150, 200, 50)
        self.lbl2.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        qle = QLineEdit(self)
        qle.setGeometry(200, 200, 200, 50)
        qle2 = QLineEdit(self)
        qle2.setGeometry(200, 300, 200, 50)

    def chooseShip(self):
        self.lbl2 = QLabel(self)
        self.lbl2.setText("Choose ship")
        self.lbl2.setGeometry(410, 150, 200, 50)
        self.lbl2.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        self.player1Cb = QComboBox(self)
        # self.player1Cb.setCursor(Qt.PointingHandCursor)
        self.player1Cb.setStyleSheet(
            "border:1px solid rgb(220, 20, 60);font-size: 20px; color: red; font-family: Helvetica;");
        self.player1Cb.addItem("")
        self.player1Cb.addItem("red")
        self.player1Cb.addItem("green")
        self.player1Cb.addItem("yellow")
        self.player1Cb.addItem("blue")
        self.player1Cb.model().item(0).setEnabled(False)
        self.player1Cb.setGeometry(410, 200, 200, 50)

        self.player2Cb = QComboBox(self)
        # self.player1Cb.setCursor(Qt.PointingHandCursor)
        self.player2Cb.setStyleSheet(
            "border:1px solid rgb(220, 20, 60);font-size: 20px; color: red; font-family: Helvetica;");
        self.player2Cb.addItem("")
        self.player1Cb.addItem("red")
        self.player1Cb.addItem("green")
        self.player1Cb.addItem("yellow")
        self.player1Cb.addItem("blue")
        self.player2Cb.model().item(0).setEnabled(False)
        self.player2Cb.setGeometry(410, 300, 200, 50)

    def labels(self):
        self.lbl3 = QtWidgets.QLabel(self)
        self.lbl3.setText("First player")
        self.lbl3.setGeometry(10, 200, 200, 50)
        self.lbl3.setStyleSheet(" color: red;font-size: 20px; font-family: Arial ;");

        self.lbl4 = QtWidgets.QLabel(self)
        self.lbl4.setText("Second player")
        self.lbl4.setGeometry(10, 300, 200, 50)
        self.lbl4.setStyleSheet(" color: red;font-size: 20px; font-family: Arial ;");

    def buttonPlay(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("PLAY")
        self.b1.setGeometry(750, 400, 200, 50)
        self.b1.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");


def wi():
    app = QApplication(sys.argv)
    win = MultiPlayerWindow()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    wi()
