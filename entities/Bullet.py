from entities.MovableCircle import MovableCircle


class Bullet(MovableCircle):
    def __init__(self, x: float, y: float, velocity: float, angle: float, r: int, color: str, player_id: str):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.color = color
        self.player_id = player_id
