from persistance.Storage import Storage
<<<<<<< Updated upstream
=======
from math import sin, cos, radians
from entities import Asteroid, Bullet, Spaceship
from datetime import datetime
from core.utils.time_helper import _convert_timestamp_to_microseconds


class MovementHandler:
    def __init__(self, timestamp: datetime):
        self.last_time_recorded = timestamp
        # prodje oko 100.000 usec izmedju poziva funkcije pa se redukuje ovde da bi objekti mogli nomalno
        # da se krecu
        self.reduction_factor = 10000
        pass

    def calculate_new_positions(self, storage: Storage, current_time: datetime):
        elapsed_time = (_convert_timestamp_to_microseconds(current_time) -
                        _convert_timestamp_to_microseconds(self.last_time_recorded)) / self.reduction_factor
        self.last_time_recorded = current_time

        for asteroid in storage.get_all_asteroids():
            asteroid.x = asteroid.x + cos(radians(asteroid.angle)) * asteroid.velocity * elapsed_time
            asteroid.y = asteroid.y + sin(radians(asteroid.angle)) * asteroid.velocity * elapsed_time
>>>>>>> Stashed changes

        for bullet in storage.get_all_bullets():
            bullet.x = bullet.x + cos(radians(bullet.angle)) * bullet.velocity * elapsed_time
            bullet.y = bullet.y + sin(radians(bullet.angle)) * bullet.velocity * elapsed_time

<<<<<<< Updated upstream
class MovementHandler:
    def __init__(self):
        pass

    def handle(self, storage: Storage, elapsed_time: float):
        pass
=======
        for spacecraft in storage.get_all_spacecrafts():
            spacecraft.x = spacecraft.x + cos(radians(spacecraft.angle)) * spacecraft.velocity * elapsed_time
            spacecraft.y = spacecraft.y + sin(radians(spacecraft.angle)) * spacecraft.velocity * elapsed_time
>>>>>>> Stashed changes
