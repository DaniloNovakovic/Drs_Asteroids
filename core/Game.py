from core.Screen import Screen
from core.LevelFactory import LevelFactory
from core.KeyHandler import KeyHandler
from core.MovementHandler import calculate_new_positions
from core.CollisionHandler import CollisionHandler
from entities.Spaceship import Spaceship
from PyQt5.QtCore import QThread
import threading
import time


class Game:
    def __init__(self, screen: Screen, level_factory: LevelFactory, key_handler: KeyHandler,
                 collision_handler: CollisionHandler):
        #TODO: playerID to be set by game server
        self.playerID = '1'
        self.screen = screen
        self.level_factory = level_factory
        self.key_handler = key_handler
        self.collision_handler = collision_handler
        self.storage = level_factory.create_new()

    def start(self):
        self.screen.keyPressed.connect(self.on_key_pressed)
        # TODO: set self.update to be called periodically (by detached thread in while loop or timer)

        #self.storage.add_spaceship(Spaceship(200, 200, 2, 0, 30, '1', self.playerID, 'green'))

        self.update(elapsed_time=300)  # for testing purposes (until we render asteroid properly)
        """
        update_thread = QThread(target=self.update_loop, args=[1])
        update_thread.start()
        """
        """
        update_thread = threading.Thread(target=self.update_loop, args=[30])
        update_thread.start()
        update_thread.join()
        """

        pass

    def on_key_pressed(self, pressed_key):
        self.key_handler.handle(self.storage, pressed_key, self.playerID)

    def update_loop(self, tick_frequency: int):
        while 1:
            self.update(1000 / tick_frequency)
            time.sleep(1 / tick_frequency)

    def update(self, elapsed_time: float):
        calculate_new_positions(storage=self.storage, elapsed_time=elapsed_time)
        self.collision_handler.handle(storage=self.storage)
        self.screen.render_storage(storage=self.storage, elapsed_time=elapsed_time)
