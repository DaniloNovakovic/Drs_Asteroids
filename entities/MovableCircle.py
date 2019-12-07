from entities.MovableObject import MovableObject


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

    def accelerate(self):
        # TODO: Vladimir increase speed
        pass

    def decelerate(self):
        # TODO: Vladimir decrease speed
        pass

    def rotate_left(self):
        # TODO: Vladimir rotate left
        pass

    def rotate_right(self):
        # TODO: Vladimir rotate right
        pass
