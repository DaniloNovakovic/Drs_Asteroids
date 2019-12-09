from persistance.Storage import Storage
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt
from entities.Bullet import Bullet
from persistance.Storage import Storage


class KeyHandler(QWidget):
    def __init__(self):
        super().__init__()
        player_id = Storage.get_first_player_id

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
            storage.add_bullet(Bullet())
        elif pressed_key == Qt.Key_Enter:
            self.update(300)