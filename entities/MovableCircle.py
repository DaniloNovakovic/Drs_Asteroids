from entities.MovableObject import MovableObject


class MovableCircle(MovableObject):
    def __init__(self, x: float, y: float, velocity: float, angle: float, r: int):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle)
        self.r = r
