from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QPainter, QImage, QPen
from PyQt5.QtWidgets import QLineEdit, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap

from entities.Asteroid import Asteroid
from persistance.Storage import Storage


class Screen(QWidget):
    keyPressed = QtCore.pyqtSignal(int)

    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.resize(x, y)
        #self.setGeometry(200, 200, 200 + x, 200 + y)
        self.setWindowTitle(name)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        self.keyPressed.emit(event.key())

    def render_storage(self, storage: Storage, elapsed_time: float = 0):
        for asteroid in storage.get_all_asteroids():
            self.drawAsteroid(asteroid)
        pass

    def drawAsteroid(self, asteroid: Asteroid):
        image = QImage(asteroid.img_abs_path)
        '''
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QPen(Qt.black, 10, Qt.SolidLine))
        painter.drawLine(100, 100, 110, 100)
        painter.end()
        '''

        label = QLabel(self)
        label.setPixmap(QPixmap.fromImage(image))
        label.move(asteroid.x, asteroid.y)
        label.show()
