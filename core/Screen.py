from PyQt5.QtWidgets import QMainWindow
from persistance.Storage import Storage


class Screen(QMainWindow):
    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.resize(x, y)
        self.setWindowTitle(name)

    def render(self, storage: Storage):
        """TODO: Render objects from storage to screen"""
        pass
