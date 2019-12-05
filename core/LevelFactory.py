from persistance.Storage import Storage


class LevelFactory:
    def __init__(self):
        pass

    def create_new(self, level_number: int = 0) -> Storage:
        return Storage()
