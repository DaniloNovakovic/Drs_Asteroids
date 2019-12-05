from entities.MovableCircle import MovableCircle


class Asteroid(MovableCircle):
    def __init__(self, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 1,
                 points: int = 1):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.points = points
