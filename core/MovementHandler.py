from persistance.Storage import Storage
from math import sin, cos, radians
from entities import Asteroid, Bullet, Spaceship


def calculate_new_positions(storage: Storage, elapsed_time: float):
    for asteroid in storage.get_all_asteroids():
        asteroid.x = asteroid.x + cos(radians(asteroid.angle)) * asteroid.velocity
        asteroid.y = asteroid.y + sin(radians(asteroid.angle)) * asteroid.velocity

    for bullet in storage.get_all_bullets():
        bullet.x = bullet.x + cos(radians(bullet.angle)) * bullet.velocity
        bullet.y = bullet.y + sin(radians(bullet.angle)) * bullet.velocity

    for spacecraft in storage.get_all_spacecrafts():
        spacecraft.x = spacecraft.x + cos(radians(spacecraft.angle)) * spacecraft.velocity
        spacecraft.y = spacecraft.y + sin(radians(spacecraft.angle)) * spacecraft.velocity


class MovementHandler:
    def __init__(self):
        pass
