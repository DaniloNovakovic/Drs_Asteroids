from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget, QLabel

from entities.MovableObject import MovableObject


class MovableCircle(MovableObject):
    def __init__(self, screen: QWidget, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 1,
                 img_abs_path: str = ""):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle)
        self.r = r
        self.img_abs_path = img_abs_path
        self.image = QImage(img_abs_path)
        self.screen = screen
        self.label = self._create_label()
        self.label.show()

    def _create_label(self):
        label = QLabel(self.screen)
        label.setPixmap(QPixmap.fromImage(self.image))
        return label

    def move(self, elapsed_time: float):
        super().move(elapsed_time)
        self.label.move(self.x, self.y)
        self.label.update()

    def move_off_screen(self):
        self.x = 0 - self.r - 100
        self.y = 0 - self.r - 100
        self.label.hide()

    def is_off_screen(self, screen_width: int, screen_height: int):
        return (self.x + self.r) < 0 or (self.x - self.r) > screen_width or \
               (self.y + self.r) < 0 or (self.y - self.r) > screen_height
