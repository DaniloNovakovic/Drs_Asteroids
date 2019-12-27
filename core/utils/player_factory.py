from PyQt5.QtWidgets import QWidget
from entities.Player import Player


class PlayerFactory:
    def __init__(self, screen: QWidget):
        self.screen = screen

    def create_player(self, player_id: str, spaceship_id: str, player_config):
        return Player(screen=self.screen, player_id=player_id, spaceship_id=spaceship_id, player_config=player_config)
