
class PlayerStatus:
    def __init__(self, screen, x, y, padding=15):
        """
        TODO: Create label with text on screen, and in `update` method update label's text
        """
        self.x = x
        self.y = y
        self.padding = padding
        self.screen = screen
        self.text = ""

    def update(self, name, num_lives, num_points):
        self.text = f"ID:{name}, L:{num_lives}, PTS:{num_points}"
        print(f"Status: {self.text}")
