from persistance.Storage import Storage
from core.utils.collision import are_circles_collided
from core.behaviors.divide_asteroid import DivideAsteroidBehavior


class CollisionHandler:
    def __init__(self, screen_width, screen_height, divide_asteroid_behavior: DivideAsteroidBehavior):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.divide_asteroid_behavior = divide_asteroid_behavior

    def handle(self, storage: Storage):
        self._handle_spacecraft_with_asteroid_collision(storage)
        self._handle_bullets_with_asteroid_collision(storage)

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

    def _handle_bullets_with_asteroid_collision(self, storage: Storage):
        new_asteroids = []
        for bullet in storage.bullets:
            for asteroid in storage.asteroids:
                if not are_circles_collided(bullet, asteroid):
                    continue
                player = storage.get_player_by_id(bullet.player_id)
                player.increase_points(asteroid.points)

                divided_asteroids = self.divide_asteroid_behavior.divide(asteroid)
                new_asteroids.extend(divided_asteroids)

                bullet.move_off_screen()
                asteroid.move_off_screen()

        storage.asteroids.extend(new_asteroids)

        # TODO: Remove elements that are out of screen
