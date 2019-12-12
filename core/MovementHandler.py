from persistance.Storage import Storage
from datetime import datetime
from core.utils.time_helper import convert_timestamp_to_microseconds


class MovementHandler:
    def __init__(self, timestamp: datetime):
        self.last_time_recorded = timestamp
        # prodje oko 100.000 usec izmedju poziva funkcije pa se redukuje ovde da bi objekti mogli nomalno
        # da se krecu
        self.reduction_factor = 10000
        pass

    def calculate_new_positions(self, storage: Storage, current_time: datetime):
        elapsed_time = (convert_timestamp_to_microseconds(current_time) -
                        convert_timestamp_to_microseconds(self.last_time_recorded)) / self.reduction_factor
        self.last_time_recorded = current_time

        for asteroid in storage.get_all_asteroids():
            asteroid.move(elapsed_time)

        for bullet in storage.get_all_bullets():
            bullet.move(elapsed_time)
            
        for spacecraft in storage.get_all_spacecrafts():
            spacecraft.move(elapsed_time)
