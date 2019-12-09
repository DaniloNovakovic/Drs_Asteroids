from Drs_Asteroids.entities.MovableCircle import MovableCircle
from Drs_Asteroids.core.utils import Enums

def _divide_asteroid(_):
    return []


class Asteroid(MovableCircle):
    def __init__(self, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 1,
                 size: int = Enums.AsteroidSize.medium, divide_asteroid=_divide_asteroid):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.size = size
        self._divide = divide_asteroid

    def divide(self):
        return self._divide(self)
