from persistance.Storage import Storage
from core.utils.collision import are_circles_collided


class CollisionHandler:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def handle(self, storage: Storage):
        self._handle_spacecraft_with_asteroid_collision(storage)
        self._handle_bullets_with_asteroid_collision(storage)
        self._handle_spacecraft_with_heat_collision(storage)
        self._remove_off_screen_elements(storage)
        self._hide_screen_elements(storage)

    @staticmethod
    def _handle_spacecraft_with_asteroid_collision(storage: Storage):
        """
        Removes life of the player if his spacecraft has hit the asteroid.
        If player has no lives left then spacecraft will be removed from screen
        """
        player1 = storage.players[0]
        player2 = storage.players[1]
        for spacecraft in storage.spacecrafts:
            for asteroid in storage.asteroids:
                if not are_circles_collided(spacecraft, asteroid):
                    continue
                player = storage.get_player_by_id(spacecraft.player_id)
                player.remove_life()
                if player.is_dead():
                    spacecraft.move_off_screen()
                    if player1.is_dead() and player2.is_dead():
                        exit()

    @staticmethod
    def _handle_spacecraft_with_heat_collision(storage: Storage):
        """
        Removes life of the player if his spacecraft has hit the asteroid.
        If player has no lives left then spacecraft will be removed from screen
        """
        for spacecraft in storage.spacecrafts:
            for heart in storage.hearts:
                if not are_circles_collided(spacecraft, heart):
                    continue
                player = storage.get_player_by_id(spacecraft.player_id)
                player.add_life()
                heart.move_off_screen()

    @staticmethod
    def _handle_bullets_with_asteroid_collision(storage: Storage):
        """
        Checks if bullet has hit asteroid.
        Upon collision asteroid will be divided or removed and player will gain points.
        """
        new_asteroids = []
        for bullet in storage.bullets:
            for asteroid in storage.asteroids:
                if not are_circles_collided(bullet, asteroid):
                    continue
                player = storage.get_player_by_id(bullet.player_id)
                player.increase_points(asteroid.points)

                divided_asteroids = asteroid.divide()
                new_asteroids.extend(divided_asteroids)

                bullet.destroy()
                asteroid.destroy()
        storage.asteroids.extend(new_asteroids)

    def _remove_off_screen_elements(self, storage: Storage):
        """Removes elements that are completely outside of screen from storage"""
        storage.spacecrafts = self._filter_out_off_screen_elements(storage.spacecrafts)

    def _hide_screen_elements(self, storage: Storage):
        storage.asteroids = self._filter_out_hidden_elements(storage.asteroids)
        storage.bullets = self._filter_out_hidden_elements(storage.bullets)

    def _filter_out_off_screen_elements(self, elements: list) -> list:
        return list(filter(lambda circle: not circle.is_off_screen(self.screen_width, self.screen_height), elements))

    def _filter_out_hidden_elements(self, elements: list) -> list:
        return list(filter(lambda circle: not circle.is_hidden(), elements))
