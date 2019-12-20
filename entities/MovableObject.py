from math import sin, cos, radians

MIN_VELOCITY = 0
MAX_VELOCITY = 3


class MovableObject:
    def __init__(self, x: float = 0, y: float = 0, velocity: float = 0, angle: float = 0):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.angle = angle

    def move(self, elapsed_time: float):
        self.x = self.x + cos(radians(self.angle)) * self.velocity * elapsed_time
        self.y = self.y + sin(radians(self.angle)) * self.velocity * elapsed_time

    def accelerate(self):
        if self.velocity < MAX_VELOCITY:
            self.velocity = self.velocity + 0.1

    def decelerate(self):
        if self.velocity > MIN_VELOCITY:
            self.velocity = self.velocity - 0.1

    def rotate_left(self):
        self.angle = (self.angle - 10) % 360

    def rotate_right(self):
        self.angle = (self.angle + 10) % 360
