from entities.MovableCircle import MovableCircle
from math import sqrt


def is_point_inside_circle(point_x: float, point_y: float, circle: MovableCircle) -> bool:
    return sqrt((point_x - circle.x) ** 2 + (point_y - circle.y) ** 2) < circle.r


def are_circles_collided(left_circle: MovableCircle, right_circle: MovableCircle) -> bool:
    distance_between_circles_squared = (right_circle.x - left_circle.x) ** 2 + (right_circle.y - left_circle.y) ** 2
    return distance_between_circles_squared < (left_circle.r + right_circle.r) ** 2


def is_circle_off_screen(circle: MovableCircle, screen_width: int, screen_height: int):
    return circle.x < 0 or circle.x > screen_width or circle.y < 0 or circle.y > screen_height
