import sys
from datetime import datetime
from multiprocessing import Queue, Process

from PyQt5.QtWidgets import QApplication

from core.CollisionHandler import CollisionHandler
from core.Game import Game
from core.KeyHandler import KeyHandler
from core.LevelFactory import LevelFactory
from core.MovementHandler import MovementHandler
from core.Screen import Screen
from core.utils.asteroid_factory import AsteroidFactory
from core.utils.bullet_factory import BulletFactory
from core.utils.heart_factory import HeartFactory
from core.utils.player_factory import PlayerFactory
from core.utils.spaceship_factory import SpaceshipFactory
from entities.PlayerInput import PlayerInput


class AsteroidsTournament:
    # TODO: Prosiri sa cim god hoces
    def __init__(self, queue: Queue, player_inputs=[], screen_width=1000, screen_height=600):
        self.queue = queue
        self.screen = Screen(screen_width, screen_height, "Asteroids")

        '''Dependency injection - here you can inject handlers/services into constructor'''

        # todo: izmeni po potrebi sta ti treba
        spaceship_factory = SpaceshipFactory(screen=self.screen)
        asteroid_factory = AsteroidFactory(screen=self.screen)
        hearts_factory = HeartFactory(screen=self.screen)
        player_factory = PlayerFactory(screen=self.screen)
        level_factory = LevelFactory(screen_width=screen_width, screen_height=screen_height,
                                     asteroid_factory=asteroid_factory,
                                     spaceship_factory=spaceship_factory,
                                     heart_factory=hearts_factory,
                                     player_factory=player_factory,
                                     player_inputs=player_inputs)
        bullet_factory = BulletFactory(screen=self.screen)
        key_handler = KeyHandler(bullet_factory=bullet_factory)
        movement_handler = MovementHandler(datetime.now(), screen_width, screen_height)
        collision_handler = CollisionHandler(screen_width=screen_width, screen_height=screen_height)

        self.game = Game(self.screen, level_factory=level_factory, key_handler=key_handler,
                         collision_handler=collision_handler, movement_handler=movement_handler,
                         on_game_end=self.on_game_end)

    def on_game_end(self, storage):
        players = storage.players
        winner = self.find_winner(players)
        self.queue.put(winner.player_id)
        self.queue.close()

    def find_winner(self, players):
        max_num_points = 0
        winner_player = None
        for player in players:
            if player.num_points > max_num_points:
                max_num_points = player.num_points
                winner_player = player
        return winner_player

    def start(self):
        self.screen.show()
        self.game.start()


def start_game(queue: Queue, player1_id, player1_color, player2_id, player2_color):
    app = QApplication(sys.argv)
    game = AsteroidsTournament(
        queue=queue,
        player_inputs=[
            PlayerInput(player_id=player1_id, color=player1_color),
            PlayerInput(player_id=player2_id, color=player2_color)
        ])
    game.start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    q = Queue()
    process = Process(target=start_game, args=(q, "Steve", "red", "Urkel", "yellow"))
    process.start()
    winner_id = q.get()
    print(winner_id)
    process.kill()
