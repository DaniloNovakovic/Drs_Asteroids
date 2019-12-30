from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("Manu")
        self.initUI()

    def initUI(self):

        self.Buttons()

    def Buttons(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("START GAME")
        self.b1.setGeometry(400, 200, 250, 50)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("SCORE")
        self.b2.setGeometry(400, 300, 250, 50)

        self.b3 = QtWidgets.QPushButton(self)
        self.b3.setText("EXIT")
        self.b3.setGeometry(400, 400, 250, 50)

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()