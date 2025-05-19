from line import Line
from collections.abc import Callable

class Wall:
    def __init__(self, line:Callable[[], Line]) -> None:
        self.__line = line
        self.visible = True
    
    def line(self):
        return self.__line()
