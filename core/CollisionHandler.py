from persistance.Storage import Storage
from core.utils.collision import are_circles_collided


class CollisionHandler:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def handle(self, storage: Storage):
        self._handle_spacecraft_with_asteroid_collision(storage)
        self._handle_bullets_with_asteroid_collision(storage)
        self._remove_off_screen_elements(storage)

    @staticmethod
    def _handle_spacecraft_with_asteroid_collision(storage: Storage):
        for spacecraft in storage.spacecrafts:
            for asteroid in storage.asteroids:
                if not are_circles_collided(spacecraft, asteroid):
                    continue
                player = storage.get_player_by_id(spacecraft.player_id)
                player.remove_life()
                if player.is_dead():
                    spacecraft.move_off_screen()
                    break

    @staticmethod
    def _handle_bullets_with_asteroid_collision(storage: Storage):
        new_asteroids = []
        for bullet in storage.bullets:
            for asteroid in storage.asteroids:
                if not are_circles_collided(bullet, asteroid):
                    continue
                player = storage.get_player_by_id(bullet.player_id)
                player.increase_points(asteroid.points)

                divided_asteroids = asteroid.divide()
                new_asteroids.extend(divided_asteroids)

                bullet.move_off_screen()
                asteroid.move_off_screen()
        storage.asteroids.extend(new_asteroids)

    def _remove_off_screen_elements(self, storage):
        pass
