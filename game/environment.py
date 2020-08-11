from game.console import Console
from game.grabscreen import grab_screen
import keyboard


class Environment:
    def __init__(self, width=630, height=460):
        self.screen_shape = (height, width)
        self.console = Console()
        self.region = (10, 50, 10+width, 50+height)
        self.paused = True
        self.size_action_space = 4
        self.done = True

    def step(self):
        pass

    def get_screen(self):
        return grab_screen(self.region)

    def reset(self):
        keyboard.press('F7')
        keyboard.press(self.console.controller.start)
        self.done = False
        self.paused = False
