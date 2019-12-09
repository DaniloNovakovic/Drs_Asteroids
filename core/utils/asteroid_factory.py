from pathlib import Path
from random import randint
from entities.Asteroid import Asteroid
from core.utils.Enums import AsteroidSize
import os


def _get_full_image_path(img_name: str) -> str:
    script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "..\\Resources\\" + img_name
    abs_file_path = Path(os.path.join(script_dir, rel_path)).resolve()
    print(abs_file_path)
    return str(abs_file_path)


def create_asteroid(asteroid_type: AsteroidSize, x=0, y=0, velocity: float = 1, angle: float = 0) -> Asteroid:
    if asteroid_type == AsteroidSize.small:
        return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=5, points=200,
                        img_abs_path=_get_full_image_path("small_asteroid.png"))
    if asteroid_type == AsteroidSize.medium:
        return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=10, points=150,
                        img_abs_path=_get_full_image_path("medium_asteroid.png"),
                        divide_asteroid=_divide_medium_asteroid)
    return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=20, points=100,
                    img_abs_path=_get_full_image_path("large_asteroid.png"), divide_asteroid=_divide_large_asteroid)


def _divide_medium_asteroid(asteroid: Asteroid) -> list:
    return _divide_asteroid(asteroid=asteroid, new_asteroid_type=AsteroidSize.small, velocity_increase=2.0)


def _divide_large_asteroid(asteroid: Asteroid) -> list:
    return _divide_asteroid(asteroid=asteroid, new_asteroid_type=AsteroidSize.medium, velocity_increase=1.5)


def _divide_asteroid(asteroid: Asteroid, new_asteroid_type: AsteroidSize, velocity_increase: float = 1.0,
                     num_new_asteroids: int = 2) -> list:
    new_asteroids = []
    for _ in range(num_new_asteroids):
        new_asteroids.append(create_asteroid(
            asteroid_type=new_asteroid_type,
            x=asteroid.x,
            y=asteroid.y,
            velocity=asteroid.velocity * velocity_increase,
            angle=_randomize_angle(asteroid.angle)
        ))
    return new_asteroids


def _randomize_angle(angle: float) -> float:
    return angle + randint(-5, 5)  # TODO: Increase randomness of this function
