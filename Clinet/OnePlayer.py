import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QMessageBox
from core.utils.image_helper import get_full_image_path






class One(QMainWindow):
    def __init__(self):
        super(One, self).__init__()
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
        self.BackGroundLabel.setGeometry(0,0,1000,600)

    def username(self):
        self.lbl2 = QtWidgets.QLabel(self)
        self.lbl2.setText("Enter name")
        self.lbl2.setGeometry(200,150,200,50)
        self.lbl2.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        qle = QLineEdit(self)
        qle.setGeometry(200,200,200,50)

    def chooseShip(self):
        self.lbl2 = QLabel(self)
        self.lbl2.setText("Choose ship")
        self.lbl2.setGeometry(410,150,200,50)
        self.lbl2.setStyleSheet(" color: white;font-size: 26px; font-family: Arial Black;");

        self.player1Cb = QComboBox(self)
        # self.player1Cb.setCursor(Qt.PointingHandCursor)
        self.player1Cb.setStyleSheet("border:1px solid rgb(220, 20, 60); color: red; font-family: Helvetica;");
        self.player1Cb.addItem("")
        self.player1Cb.addItem("Space1")
        self.player1Cb.addItem("Space2")

        self.player1Cb.model().item(0).setEnabled(False)
        self.player1Cb.setGeometry(410,200,200,50)

    def buttonPlay(self):
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("PLAY")
        self.b1.setGeometry(750, 400, 200, 50)
        self.b1.setStyleSheet( "border:2px solid rgb(120, 20, 60); color: blue;font-size: 26px; font-family: Arial Black;");

def wi():
    app = QApplication(sys.argv)
    win = One()

    win.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = One()
    ex.show()
    sys.exit(app.exec_())