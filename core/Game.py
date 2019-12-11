from core.Screen import Screen
from core.LevelFactory import LevelFactory
from core.KeyHandler import KeyHandler
from core.MovementHandler import MovementHandler
from core.CollisionHandler import CollisionHandler
<<<<<<< Updated upstream
=======
from entities.Spaceship import Spaceship
from PyQt5.QtCore import QThread, Qt, pyqtSignal
import threading
>>>>>>> Stashed changes
import time
from datetime import datetime


class CounterThread(QThread):
    game_tick = pyqtSignal(datetime)
    tick_frequency = 10

    def run(self):
        while 1:
            self.game_tick.emit(datetime.now())
            time.sleep(float(1 / self.tick_frequency))


class Game:
    def __init__(self, screen: Screen, level_factory: LevelFactory, key_handler: KeyHandler,
<<<<<<< Updated upstream
                 movement_handler: MovementHandler, collision_handler: CollisionHandler):
=======
                 collision_handler: CollisionHandler, movement_handler: MovementHandler):
        # TODO: playerID to be set by game server
        self.playerID = '1'
>>>>>>> Stashed changes
        self.screen = screen
        self.level_factory = level_factory
        self.key_handler = key_handler
        self.movement_handler = movement_handler
        self.collision_handler = collision_handler
        self.storage = level_factory.create_new()
        self.movement_handler = movement_handler
        self.update_thread = CounterThread()

    def start(self):
        self.screen.keyPressed.connect(self.on_key_pressed)
        # TODO: set self.update to be called periodically (by detached thread in while loop or timer)
<<<<<<< Updated upstream
        self.update(elapsed_time=0)  # for testing purposes (until we render asteroid properly)
        # self.update_loop(tick_frequency=30)
=======
        self.update_thread.game_tick.connect(self.update)
        self.update_thread.start()

        # self.storage.add_spaceship(Spaceship(200, 200, 2, 0, 30, '1', self.playerID, 'green'))

        #self.update(elapsed_time=300)  # for testing purposes (until we render asteroid properly)
        """
        update_thread = QThread(target=self.update_loop, args=[1])
        update_thread.start()
        """
        """
        update_thread = threading.Thread(target=self.update_loop, args=[30])
        update_thread.start()
        update_thread.join()
        """

>>>>>>> Stashed changes
        pass

    def on_key_pressed(self, pressed_key):
        self.key_handler.handle(self.storage, pressed_key)

    def update_loop(self, tick_frequency: int):
        while ():
            self.update(1000 / tick_frequency)
            time.sleep(1 / tick_frequency)

<<<<<<< Updated upstream
    def update(self, elapsed_time: float):
        self.movement_handler.handle(storage=self.storage, elapsed_time=elapsed_time)
=======
    def update(self, current_time: datetime):
        print('tick')
        # TODO: clear the screen before every update
        self.movement_handler.calculate_new_positions(storage=self.storage, current_time=current_time)
>>>>>>> Stashed changes
        self.collision_handler.handle(storage=self.storage)
        self.screen.render_storage(storage=self.storage)
