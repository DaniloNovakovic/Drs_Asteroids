from PyQt5.QtWidgets import QWidget

from entities.MovableCircle import MovableCircle


class Spaceship(MovableCircle):
    def __init__(self, screen: QWidget, x: float, y: float, velocity: float, angle: float, r: int, spaceship_id: str,
                 player_id: str, img_abs_path: str = ""):
        super().__init__(screen=screen, img_abs_path=img_abs_path, x=x, y=y, velocity=velocity, angle=angle, r=r)
        self.spaceship_id = spaceship_id
        self.player_id = player_id
