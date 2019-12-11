from entities.MovableCircle import MovableCircle


class Spaceship(MovableCircle):
    def __init__(self, x: float, y: float, velocity: float, angle: float, r: int, spaceship_id: str,
                 player_id: str, color: str, img_abs_path: str = ""):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.spaceship_id = spaceship_id
        self.player_id = player_id
        self.color = color
        self.img_abs_path = img_abs_path
