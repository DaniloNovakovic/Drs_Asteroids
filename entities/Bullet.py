from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from entities.MovableCircle import MovableCircle


class Bullet(MovableCircle):
    def __init__(self, x: int = 0, y: int = 0, velocity: float = 0, angle: float = 0, r: int = 0,
                 player_id: str = "", color: str = "", img_abs_path: str = ""):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.color = color
        self.player_id = player_id
        self.img_abs_path = img_abs_path
        self.image = QImage(self.img_abs_path)
        self.label = None

    def draw(self, screen: QWidget):
        if self.label is None:
            self.label = QLabel(screen)
            self.label.setPixmap(QPixmap.fromImage(self.image))
        self.label.move(self.x, self.y)
        self.label.show()