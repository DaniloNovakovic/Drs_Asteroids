from core.utils import bullet_factory
from PyQt5.QtWidgets import (QWidget)
from PyQt5.Qt import Qt
from persistance.Storage import Storage


class KeyHandler(QWidget):
    def __init__(self):
        super().__init__()

    def handle(self, storage: Storage, pressed_key, player_id):
        spaceship = storage.get_spaceship_by_player_id(player_id)
        if pressed_key == Qt.Key_Up:
            spaceship.accelerate()
        elif pressed_key == Qt.Key_Down:
            spaceship.decelerate()
        elif pressed_key == Qt.Key_Left:
            spaceship.rotate_left()
        elif pressed_key == Qt.Key_Right:
            spaceship.rotate_right()
        elif pressed_key == Qt.Key_Space:
            storage.add_bullet(bullet_factory.create_bullet(player_id=player_id, color='red',
                                                            x=spaceship.x, y=spaceship.y, angle=spaceship.angle))
        elif pressed_key == Qt.Key_Enter:
            self.update(300)
