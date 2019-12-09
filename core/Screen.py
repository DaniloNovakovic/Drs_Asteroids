from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QImage
from PyQt5.QtWidgets import QLineEdit, QWidget
from entities.Asteroid import Asteroid
from persistance.Storage import Storage


class Screen(QWidget):
    keyPressed = QtCore.pyqtSignal(int)

    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.resize(x, y)
        self.setWindowTitle(name)
        self.le = QLineEdit(self)
        self.le.move(130, 22)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())

    def render_storage(self, storage: Storage, elapsed_time: float = 0):
        self.le.setText(str(elapsed_time))

        asteroids = storage.get_all_asteroids()
        spacecrafts = storage.get_all_spacecrafts()

        painter = QPainter(self)

        for asteroid in asteroids:
            self.drawAsteroid(painter, asteroid)
        pass

    def drawAsteroid(self, painter: QPainter, asteroid: Asteroid):
        """TODO: Fix error where image is not displayed on screen properly"""

        src_image = QImage(asteroid.img_abs_path)
        if src_image.isNull():
            print("Failed to load image %s" % asteroid.img_abs_path)
        painter.begin(self)

        painter.drawImage(QPoint(100, 100), src_image)
        painter.end()
