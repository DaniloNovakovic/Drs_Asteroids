from Drs_Asteroids.entities.Bullet import Bullet
from Drs_Asteroids.core.utils.image_helper import _get_full_image_path


def create_bullet(player_id: str, color: str, x: int = 0, y: int = 0, velocity: float = 0,
                  angle: float = 0, r: int = 5):
    if color == 'red':
        return Bullet(x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id, color=color,
                      img_abs_path=_get_full_image_path("bullet_red.png"))
    elif color == 'green':
        return Bullet(x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id, color=color,
                      img_abs_path=_get_full_image_path("bullet_green.png"))
    elif color == 'yellow':
        return Bullet(x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id, color=color,
                      img_abs_path=_get_full_image_path("bullet_yellow.png"))
    elif color == 'blue':
        return Bullet(x=x, y=y, velocity=velocity, angle=angle, r=r, player_id=player_id, color=color,
                      img_abs_path=_get_full_image_path("bullet_blue.png"))
