from entities.Asteroid import Asteroid

SMALL_ASTEROID = 0
MEDIUM_ASTEROID = 1
LARGE_ASTEROID = 2


def create_asteroid(asteroid_type: int, x=0, y=0, velocity=1, angle=0) -> Asteroid:
    if asteroid_type == SMALL_ASTEROID:
        return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=5, points=200)
    if asteroid_type == MEDIUM_ASTEROID:
        return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=10, points=150)
    return Asteroid(x=x, y=y, velocity=velocity, angle=angle, r=20, points=100)
