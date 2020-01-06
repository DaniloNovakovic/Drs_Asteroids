from PyQt5.QtWidgets import QWidget
from entities.Player import Player
from entities.PlayerStatus import PlayerStatus


class PlayerFactory:
    def __init__(self, screen: QWidget):
        self.screen = screen

    def create_player(self, player_id: str, spaceship_id: str, player_config, status_x=15, status_y=15):
        status = PlayerStatus(screen=self.screen, x=status_x, y=status_y)
        return Player(screen=self.screen, player_id=player_id, spaceship_id=spaceship_id,
                      player_config=player_config, player_status=status)
