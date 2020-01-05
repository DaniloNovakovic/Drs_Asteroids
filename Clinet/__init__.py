import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox
from Clinet.OnePlayer import One
from Clinet.MultiPlayer import Multi
from core.utils.image_helper import get_full_image_path




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
        self.b1.clicked.connect(self.on_push_button)
        self.dialog= OnePlayerWindow(self)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText("MULITPLAYER")
        self.b2.setGeometry(400, 200, 250, 50)
        self.b2.setStyleSheet(
            "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");
        self.b2.clicked.connect(self.on_push_button2)
        self.dialog2 = TwoPlayerWindow(self)

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

    def on_push_button(self):
        self.dialog.show()
    def on_push_button2(self):
        self.dialog2.show()

    def initWindow(self):
        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def quit(self):
        app = QApplication.instance()
        app.closeAllWindows()

class OnePlayerWindow(One):
    def __init__(self,parent=None):
        super(OnePlayerWindow, self).__init__()

class TwoPlayerWindow(Multi):
    def __init__(self,parent=None):
        super(TwoPlayerWindow, self).__init__()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())


window()
