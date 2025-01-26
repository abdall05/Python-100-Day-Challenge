from turtle import Screen

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("Snake Game")
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.tracer(0)
        self.screen.bgcolor("black")
        # Disable resizing externally (Windows)
        self.screen._root.resizable(False, False)

    def __getattr__(self, name):
        return getattr(self.screen, name)
