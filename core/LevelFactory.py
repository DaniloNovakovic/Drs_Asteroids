from persistance.Storage import Storage
from Drs_Asteroids.core.utils.Enums import AsteroidSize


class LevelFactory:
    def __init__(self):
        pass

    def create_new(self, level_number: int = 0) -> Storage:
        storage = Storage()
        storage.add_asteroid(AsteroidSize.medium)
        return storage
