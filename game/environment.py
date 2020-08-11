from game.console import Console
from game.grabscreen import grab_screen
import numpy as np


class Environment:
    def __init__(self, width=630, height=460):
        self.console = Console()
        self.region = (10, 50, 10+width, 50+height)

        state: np.ndarray = None
        
    def get_screen(self):
        return grab_screen(self.region)
