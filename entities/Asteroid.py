from entities.MovableCircle import MovableCircle


class Asteroid(MovableCircle):
    def __init__(self, x: float, y: float, velocity: float, angle: float, r: int, points: int = 1):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.points = points
