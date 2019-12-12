from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QImage, QPen
from PyQt5.QtWidgets import QLineEdit, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

from entities import Asteroid, Spaceship, Bullet
from persistance.Storage import Storage


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

    def render_storage(self, storage: Storage):
        # TODO: implement drawing with QPainter
        for asteroid in storage.get_all_asteroids():
            asteroid.draw(self)

        for spaceship in storage.get_all_spacecrafts():
            spaceship.draw(self)

        for bullet in storage.get_all_bullets():
            bullet.draw(self)
