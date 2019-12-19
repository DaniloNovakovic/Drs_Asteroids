from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget


class Screen(QWidget):
    keyPressed = QtCore.pyqtSignal(int)

    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.resize(x, y)
        # self.setGeometry(200, 200, 200 + x, 200 + y)
        self.setWindowTitle(name)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())
