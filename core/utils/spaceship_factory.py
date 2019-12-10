from Drs_Asteroids.entities.Spaceship import Spaceship
from Drs_Asteroids.core.utils.image_helper import _get_full_image_path


def create_spaceship(spaceship_id: str, player_id: str, color: str, x: int = 100, y: int = 100,
                     velocity: float = 0, angle: float = 0):
    if color == 'red':
        return Spaceship(x=x, y=y, velocity=velocity, angle=angle, r=30, spaceship_id=spaceship_id,
                              player_id=player_id, color='red',
                              img_abs_path=_get_full_image_path("spaceship_red.png"))
    elif color == 'green':
        return Spaceship(x=x, y=y, velocity=velocity, angle=angle, r=30,
                         spaceship_id=spaceship_id, player_id=player_id, color='green',
                         img_abs_path=_get_full_image_path("spaceship_green.png"))
    elif color == 'yellow':
        return Spaceship(x=x, y=y, velocity=velocity, angle=angle, r=30,
                         spaceship_id=spaceship_id, player_id=player_id, color='yellow',
                         img_abs_path=_get_full_image_path("spaceship_yellow.png"))
    else:
        return Spaceship(x=x, y=y, velocity=velocity, angle=angle, r=30,
                         spaceship_id=spaceship_id, player_id=player_id, color='blue',
                         img_abs_path=_get_full_image_path("spaceship_blue.png"))
