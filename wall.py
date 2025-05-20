from line import Line
from collections.abc import Callable
from wall_index import WALLINDEX
from maze_path import Position
class Wall:
    def __init__(self, wall_index:WALLINDEX, line:Callable[[], Line], neighbor:Position|None = None) -> None:
        self._wall_index = wall_index
        self.__line = line
        self.visible = True
        self._neighbor = neighbor
    
    def line(self) -> Line:
        return self.__line()
