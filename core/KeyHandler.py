from persistance.Storage import Storage
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt


class KeyHandler(QWidget):
    def __init__(self):
        super().__init__()

    def handle(self, storage: Storage, pressed_key):
        if pressed_key == Qt.Key_Up:
            self.go_front()
        elif pressed_key == Qt.Key_Down:
            self.go_back()
        elif pressed_key == Qt.Key_Left:
            self.go_left()
        elif pressed_key == Qt.Key_Right:
            self.go_right()
        elif pressed_key == Qt.Key_Space:
            self.shoot()

    def go_front(self):
        print('Front')

    def go_back(self):
        print('Back')

    def go_left(self):
        print('Left')

    def go_right(self):
        print('Right')

    def shoot(self):
        print('Shoot')
