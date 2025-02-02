from turtle import Screen
SCREEN_HEIGHT = 491
SCREEN_WIDTH = 725
bgpic_path = "blank_states_img.gif"
class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("U.S. States Game")
        self.screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
        self.screen.tracer(0)
        self.screen.bgpic(bgpic_path)
        # Disable resizing externally (Windows)
        self.screen._root.resizable(False, False)


    def __getattr__(self, name):
        return getattr(self.screen, name)
