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
        self.screen.keyPressed.connect(self.on_key_pressed)
        # TODO: set self.update to be called periodically (by detached thread in while loop or timer)
        self.update(elapsed_time=300)
        pass

    def on_key_pressed(self, pressed_key):
        self.key_handler.handle(self.storage, pressed_key)

    def update(self, elapsed_time: float):
        self.movement_handler.handle(storage=self.storage, elapsed_time=elapsed_time)
        self.collision_handler.handle(storage=self.storage)
        self.screen.render(storage=self.storage)
