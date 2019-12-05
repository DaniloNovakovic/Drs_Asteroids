from entities.MovableObject import MovableObject


class MovableCircle(MovableObject):
    def __init__(self, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 1):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle)
        self.r = r
