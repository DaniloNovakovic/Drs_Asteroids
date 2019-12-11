from persistance.Storage import Storage
from core.utils.Enums import AsteroidSize
from core.utils import asteroid_factory


class LevelFactory:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def create_new(self, level_number: int = 0) -> Storage:
<<<<<<< Updated upstream
        asteroids = self._create_new_asteroids(num_asteroids=level_number + 1)
        return Storage(asteroids=asteroids)
=======
        asteroids = self._create_new_asteroids(num_asteroids=level_number + 5)
        player1 = Player(player_id='1', spaceship_id='1')
        player2 = Player('2', '2')
        player3 = Player('3', '3')
        player4 = Player('4', '4')
        ship1 = spaceship_factory.create_spaceship('1', '1', 'red', x=100, y=80, velocity=1)
        ship2 = spaceship_factory.create_spaceship('2', '2', 'blue', x=300, y=80, velocity=5)
        ship3 = spaceship_factory.create_spaceship('3', '3', 'yellow', x=100, y=250, velocity=10)
        ship4 = spaceship_factory.create_spaceship('4', '4', 'green', x=300, y=250, velocity=20)
        bullet1 = bullet_factory.create_bullet('1', 'red', x=120, y=40)
        bullet2 = bullet_factory.create_bullet('1', 'blue', x=300, y=40)
        bullet3 = bullet_factory.create_bullet('1', 'yellow', x=100, y=200)
        bullet4 = bullet_factory.create_bullet('1', 'green', x=325, y=210)

        #ship2 = Spaceship(100, 100, 0, 0, 30, '1', '1', 'red')
        return Storage(asteroids=asteroids, players=[player1, player2, player3, player4],
                       spacecrafts=[ship1, ship2, ship3, ship4],
                       bullets=[bullet1, bullet2, bullet3, bullet4])
>>>>>>> Stashed changes

    def _create_new_asteroids(self, num_asteroids: int = 1) -> list:
        asteroids = []
        for _ in range(num_asteroids):
            # TODO: Randomize x,y for asteroid based on screen_width & screen_height
            asteroids.append(asteroid_factory.create_asteroid(AsteroidSize.medium, x=300, y=300))
        return asteroids
