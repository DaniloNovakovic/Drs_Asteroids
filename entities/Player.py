from entities.PlayerConfig import PlayerConfig
from PyQt5.QtWidgets import QWidget
from core.utils.heart_factory import HeartFactory


class Player:
    def __init__(self, player_id: str, spaceship_id: str, player_config: PlayerConfig = None, num_points: int = 0
                 , num_lives: int = 3, screen: QWidget = None):
        self.player_id = player_id
        self.spaceship_id = spaceship_id
        self.num_points = num_points
        self.num_lives = num_lives
        self.player_config = player_config
        self.screen = screen
        self.heart_factory = HeartFactory(self.screen)
        self.hearts1 = self.create_hearts1()
        self.hearts2 = self.create_hearts2()

    def create_hearts1(self):
        if self.player_id == '1':
            for i in range(self.num_lives):
                heart1 = self.heart_factory.create_heart(player_id='1', x=15+i*30, y=15)
            return heart1

    def create_hearts2(self):
        if self.player_id == '2':
            for i in range(self.num_lives):
                heart2 = self.heart_factory.create_heart(player_id='1', x=920 + i * 30, y=15)
            return heart2

    def remove_life(self):
        self.num_lives -= 1
        if self.player_id == '1':
            self.hearts1.label.hide()
        if self.player_id == '2':
            self.hearts2.label.hide()

    def add_life(self):
        self.num_lives += 1
        self.create_hearts1()
        self.create_hearts2()

    def increase_points(self, num_points_to_add: int):
        self.num_points += num_points_to_add

    def is_dead(self) -> bool:
        return self.num_lives <= 0

    #ovde da bude srca koliko zivota ima
