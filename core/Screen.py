from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from persistance.Storage import Storage


class Screen(QMainWindow):
    keyPressed = QtCore.pyqtSignal(int)

    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.resize(x, y)
        self.setWindowTitle(name)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())

    def render(self, storage: Storage):
        """TODO: Render objects from storage to screen"""
        pass
