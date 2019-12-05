from random import randint
from entities.Asteroid import Asteroid

SMALL_ASTEROID = 0
MEDIUM_ASTEROID = 1
LARGE_ASTEROID = 2


def create_asteroid(asteroid_type: int, x=0, y=0, velocity: float = 1, angle: float = 0) -> Asteroid:
    if asteroid_type == SMALL_ASTEROID:
        return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=5, points=200)
    if asteroid_type == MEDIUM_ASTEROID:
        return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=10, points=150,
                        divide_asteroid=_divide_medium_asteroid)
    return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=20, points=100, divide_asteroid=_divide_large_asteroid)


def _divide_medium_asteroid(asteroid: Asteroid) -> list:
    return _divide_asteroid(asteroid=asteroid, new_asteroid_type=SMALL_ASTEROID, velocity_increase=2.0)


def _divide_large_asteroid(asteroid: Asteroid) -> list:
    return _divide_asteroid(asteroid=asteroid, new_asteroid_type=MEDIUM_ASTEROID, velocity_increase=1.5)


def _divide_asteroid(asteroid: Asteroid, new_asteroid_type: int, velocity_increase: float = 1.0,
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
