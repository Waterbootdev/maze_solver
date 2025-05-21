from collections.abc import Callable
from collections import namedtuple

Position = namedtuple('Position', ['x', 'y'])

class MazePath:
    def __init__(self, start: Position, 
                 set_visited:Callable[[Position|None], None], 
                 set_invisited:Callable[[Position|None], None], 
                 is_visited:Callable[[Position],bool], 
                 is_other_visited:Callable[[Position], bool],
                ) -> None:
       
        self._set_visited = set_visited
        self._set_invisited = set_invisited
        self._is_visited = is_visited
        self._is_other_visited = is_other_visited
        self._position = start
        self.__path = []

    def append(self, position:Position|None):
        if position:
            self.__path.append(self._position)
            self._position = position
        else:
            raise Exception()

   
    def step_back(self) -> bool:
        if self.__path == []:
            return False
        else:
            self._position = self.__path[-1]
            del self.__path[-1]
            return True
    
    def length(self) -> int:
        return len(self.__path) 