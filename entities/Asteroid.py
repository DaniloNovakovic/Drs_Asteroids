from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from entities.MovableCircle import MovableCircle


def _divide_asteroid(_):
    return []


class Asteroid(MovableCircle):
    def __init__(self, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 1,
                 points: int = 1, img_abs_path: str = "", divide_asteroid=_divide_asteroid):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.points = points
        self.img_abs_path = img_abs_path
        self._divide = divide_asteroid
        self.image = QImage(self.img_abs_path)
        self.label = None

    def divide(self):
        return self._divide(self)

    def draw(self, screen: QWidget):
        if self.label is None:
            self.label = QLabel(screen)
            self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.move(self.x, self.y)
        self.label.show()
