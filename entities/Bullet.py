from entities.MovableCircle import MovableCircle


class Bullet(MovableCircle):
    def __init__(self, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 0,
                 player_id: str = "", color: str = "",):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.color = color
        self.player_id = player_id
