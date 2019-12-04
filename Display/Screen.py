from PyQt5.QtWidgets import QMainWindow


class Screen(QMainWindow):
    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.resize(x, y)
        self.setWindowTitle(name)
