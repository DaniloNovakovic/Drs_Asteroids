from entities.MovableObject import MovableObject
from math import sin, cos, radians


class MovableCircle(MovableObject):
    def __init__(self, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0, r: int = 1):
        super().__init__(x=x, y=y, velocity=velocity, angle=angle)
        self.r = r

    def move_off_screen(self):
        self.x = 0 - self.r - 100
        self.y = 0 - self.r - 100

    def is_off_screen(self, screen_width: int, screen_height: int):
        return (self.x + self.r) < 0 or (self.x - self.r) > screen_width or \
               (self.y + self.r) < 0 or (self.y - self.r) > screen_height

    def move(self, elapsed_time: float):
        self.x = self.x + cos(radians(self.angle)) * self.velocity * elapsed_time
        self.y = self.y + sin(radians(self.angle)) * self.velocity * elapsed_time

    def accelerate(self):
        self.velocity = self.velocity + 0.1

    def decelerate(self):
        self.velocity = self.velocity - 0.1

    def rotate_left(self):
        self.angle = self.angle + 0.4

    def rotate_right(self):
        self.angle = self.angle - 0.4
