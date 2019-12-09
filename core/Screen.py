from PyQt5 import QtCore
import os
from PyQt5.QtCore import QRectF, QPoint, Qt
from PyQt5.QtGui import QPainter, QImage, QPen, QPixmap
from PyQt5.QtWidgets import QMainWindow
from persistance.Storage import Storage
from Drs_Asteroids.core.utils.Enums import AsteroidSize


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
        asteroids = storage.get_all_asteroids()
        spacecrafts = storage.get_all_spacecrafts()

        painter = QPainter(self)
        painter.begin(self)

        for asteroid in asteroids:
            self.drawAsteroid(painter, asteroid)

        painter.end()
        pass

    def drawAsteroid(self, painter: QPainter, asteroid):
        if asteroid.size == AsteroidSize.large:
            imgName = "large_asteroid.png"
        elif asteroid.size == AsteroidSize.medium:
            imgName = "medium_asteroid.png"
        elif asteroid.size == AsteroidSize.small:
            imgName = "small_asteroid.png"

        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "Resources\\" + imgName
        abs_file_path = os.path.join(script_dir, rel_path)
        print(abs_file_path)
        srcImage = QImage(abs_file_path)
        if srcImage.isNull():
            print("Failed to load image %s" % abs_file_path)
        painter.begin(self)
        """Ne prikazuje nikakvu sliku"""
        painter.drawImage(QPoint(100, 100), srcImage)
        painter.end()
