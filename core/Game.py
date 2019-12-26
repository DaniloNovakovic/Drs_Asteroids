from core.Screen import Screen
from core.LevelFactory import LevelFactory
from core.KeyHandler import KeyHandler
from core.MovementHandler import MovementHandler
from core.CollisionHandler import CollisionHandler
from PyQt5.QtCore import QThread, pyqtSignal
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
                 collision_handler: CollisionHandler, movement_handler: MovementHandler):
        # TODO: playerID to be set by game server
        self.playerID = '1'
        self.playerID2 = '2'
        self.screen = screen
        self.level_factory = level_factory
        self.key_handler = key_handler
        self.collision_handler = collision_handler
        self.game_level = 1
        self.storage = level_factory.create_new(self.game_level)
        self.movement_handler = movement_handler
        self.update_thread = CounterThread()

    def start(self):
        self.screen.keyPressed.connect(self.on_key_pressed)
        self.update_thread.game_tick.connect(self.update)
        self.update_thread.start()

    def on_key_pressed(self, pressed_key):
        self.key_handler.handle(self.storage, pressed_key)

    def update(self, current_time: datetime):
        self.movement_handler.calculate_new_positions(storage=self.storage, current_time=current_time)
        self.collision_handler.handle(storage=self.storage)
        self.new_level(self.game_level)

    def new_level(self, game_level):
        if len(self.storage.asteroids) == 0:
            self.game_level = game_level + 1
            for spacecraft in self.storage.spacecrafts:
                spacecraft.label.hide()
            for bullet in self.storage.bullets:
                bullet.label.hide()
            self.storage.spacecrafts.clear()
            self.storage.bullets.clear()
            self.storage = self.level_factory.create_new(self.game_level)
