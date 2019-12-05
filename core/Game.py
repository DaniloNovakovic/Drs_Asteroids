from core.Screen import Screen
from core.LevelFactory import LevelFactory
from core.KeyHandler import KeyHandler
from core.MovementHandler import MovementHandler
from core.CollisionHandler import CollisionHandler


class Game:
    def __init__(self, screen: Screen, level_factory: LevelFactory, key_handler: KeyHandler,
                 movement_handler: MovementHandler, collision_handler: CollisionHandler):
        self.screen = screen
        self.level_factory = level_factory
        self.key_handler = key_handler
        self.movement_handler = movement_handler
        self.collision_handler = collision_handler
        self.storage = level_factory.create_new()

    def start(self):
        """TODO: Add timer & attach key pressed event handler"""
        pass

    def update(self, elapsed_time: float):
        self.movement_handler.handle(storage=self.storage, elapsed_time=elapsed_time)
        self.collision_handler.handle(storage=self.storage)
        self.screen.render(storage=self.storage)
