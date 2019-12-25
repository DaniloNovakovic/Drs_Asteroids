from PyQt5.Qt import Qt


class PlayerConfig:
    def __init__(self, key_left=Qt.Key_Left, key_right=Qt.Key_Right,
                 key_down=Qt.Key_Down, key_up=Qt.Key_Up, key_shoot=Qt.Key_Space):
        self.key_left = key_left
        self.key_right = key_right
        self.key_down = key_down
        self.key_up = key_up
        self.key_shoot = key_shoot
