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
            self.draw_asteroid(asteroid)

        for spaceship in storage.get_all_spacecrafts():
            self.draw_spaceship(spaceship)

        for bullet in storage.get_all_bullets():
            self.draw_bullet(bullet)

    def draw_asteroid(self, asteroid: Asteroid):
        image = QImage(asteroid.img_abs_path)
        label = QLabel(self)
        label.setPixmap(QPixmap.fromImage(image))
        label.move(asteroid.x, asteroid.y)
        label.show()
        '''
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        painter.drawLine(100, 100, 110, 100)
        painter.end()
        '''

    def draw_spaceship(self, spaceship: Spaceship):
        image = QImage(spaceship.img_abs_path)
        label = QLabel(self)
        label.setPixmap(QPixmap.fromImage(image))
        label.move(spaceship.x, spaceship.y)
        label.show()

    def draw_bullet(self, bullet: Bullet):
        image = QImage(bullet.img_abs_path)
        label = QLabel(self)
        label.setPixmap(QPixmap.fromImage(image))
        label.move(bullet.x, bullet.y)
        label.show()
