from PyQt5.Qt import Qt

from core.utils.bullet_factory import BulletFactory
from persistance.Storage import Storage


class KeyHandler:
    def __init__(self, bullet_factory: BulletFactory):
        super().__init__()
        self.bullet_factory = bullet_factory

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
            storage.add_bullet(self.bullet_factory.create_bullet(player_id=player_id, color='red',
                                                                 x=spaceship.x, y=spaceship.y,
                                                                 angle=spaceship.angle))
