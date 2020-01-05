from PyQt5 import QtCore,QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from core.utils.image_helper import get_full_image_path


class Screen(QWidget):
    keyPressed = QtCore.pyqtSignal(int)

    def __init__(self, x: int, y: int, name: str,img_abs_path: str = ""):
        super().__init__()
        self.resize(x, y)

        # self.setGeometry(200, 200, 200 + x, 200 + y)
        self.setWindowTitle(name)

        self.BackGround = QPixmap(get_full_image_path("galaxy.jpg"))
        self.BackGroundLabel = QtWidgets.QLabel(self)
        self.BackGroundLabel.setPixmap(self.BackGround)
        self.BackGroundLabel.setGeometry(0, 0, 1000, 600)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())

