class Storage:
    def __init__(self, asteroids=(), players=(), spacecrafts=(), bullets=()):
        self.asteroids = list(asteroids)
        self.players = list(players)
        self.spacecrafts = list(spacecrafts)
        self.bullets = list(bullets)