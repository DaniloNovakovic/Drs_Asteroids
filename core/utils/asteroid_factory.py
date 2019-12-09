from random import randint
from Drs_Asteroids.entities.Asteroid import Asteroid
from Drs_Asteroids.core.utils.Enums import AsteroidSize


def create_asteroid(asteroid_type: AsteroidSize, x=0, y=0, velocity: float = 1, angle: float = 0) -> Asteroid:
    return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=5, size=asteroid_type)


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
