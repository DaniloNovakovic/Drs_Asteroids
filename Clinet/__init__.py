import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox




class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("Manu")
        self.initUI()

    def initUI(self):
        self.initWindow()
        self.Buttons()

    def Buttons(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("START GAME")
        self.b1.setGeometry(400, 100, 250, 50)
        self.b1.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("MULITPLAYER")
        self.b2.setGeometry(400, 200, 250, 50)
        self.b2.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("SCORE")
        self.b2.setGeometry(400, 300, 250, 50)
        self.b2.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("EXIT")
        self.b3.setGeometry(400, 400, 250, 50)
        self.b3.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.b3.clicked.connect(self.quit)

    def initWindow(self):
        self.BackGround = QPixmap("galaxy.jpg")
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def quit(self):
        app = QApplication.instance()
        app.closeAllWindows()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
