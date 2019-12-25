from PyQt5.Qt import Qt

from core.utils.bullet_factory import BulletFactory
from persistance.Storage import Storage


class KeyHandler:
    def __init__(self, bullet_factory: BulletFactory):
        super().__init__()
        self.bullet_factory = bullet_factory

    def handle(self, storage: Storage, pressed_key):
        for spacecraft in storage.spacecrafts:
            player = storage.get_player_by_spaceship(spacecraft)
            if pressed_key == player.player_config.key_left:
                spacecraft.rotate_left()
            elif pressed_key == player.player_config.key_right:
                spacecraft.rotate_right()
            elif pressed_key == player.player_config.key_up:
                spacecraft.accelerate()
            elif pressed_key == player.player_config.key_down:
                spacecraft.decelerate()
            elif pressed_key == player.player_config.key_shoot:
                storage.add_bullet(self.bullet_factory.create_bullet(player_id=player.player_id, color='red',
                                                                        x=spacecraft.x, y=spacecraft.y,
                                                                        angle=spacecraft.angle))
