from PyQt5.Qt import Qt

from core.utils.bullet_factory import BulletFactory
from persistance.Storage import Storage


class KeyHandler:
    def __init__(self, bullet_factory: BulletFactory):
        super().__init__()
        self.bullet_factory = bullet_factory

    def handle(self, storage: Storage, pressed_key, player_id, player_id2):
        spaceship = storage.get_spaceship_by_player_id(player_id)
        spaceship2 = storage.get_spaceship_by_player_id(player_id2)
        if pressed_key == Qt.Key_Up:
            spaceship.accelerate()
        elif pressed_key == Qt.Key_Down:
            spaceship.decelerate()
        elif pressed_key == Qt.Key_Left:
            spaceship.rotate_left()
        elif pressed_key == Qt.Key_Right:
            spaceship.rotate_right()
        elif pressed_key == Qt.Key_Space:
            storage.add_bullet(self.bullet_factory.create_bullet(player_id=player_id, color='red',
                                                                 x=spaceship.x, y=spaceship.y,
                                                                 angle=spaceship.angle))

        elif pressed_key == Qt.Key_W:
            spaceship2.accelerate()
        elif pressed_key == Qt.Key_S:
            spaceship2.decelerate()
        elif pressed_key == Qt.Key_A:
            spaceship2.rotate_left()
        elif pressed_key == Qt.Key_D:
            spaceship2.rotate_right()
        elif pressed_key == Qt.Key_Control:
            storage.add_bullet(self.bullet_factory.create_bullet(player_id=player_id2, color='yellow',
                                                                 x=spaceship2.x, y=spaceship2.y,
                                                                 angle=spaceship2.angle))
