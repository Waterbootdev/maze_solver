from window import Window
from point import Point
from line import Line
from wall import Wall
from wall_index import WALLINDEX



class Cell:
    def __init__(self, window = None) -> None:
                
        self.__walls = {}

        self.__walls[WALLINDEX.TOP] = Wall(WALLINDEX.TOP, self.top_wall) 
        self.__walls[WALLINDEX.RIGHT] = Wall(WALLINDEX.RIGHT, self.right_wall) 
        self.__walls[WALLINDEX.BOTTOM] = Wall(WALLINDEX.BOTTOM, self.bottom_wall) 
        self.__walls[WALLINDEX.LEFT] = Wall(WALLINDEX.LEFT, self.left_wall) 

        self.__left = -1
        self.__top = -1
        self.__right = -1
        self.__bottom = -1

        self.__window = window

        self.entrans_visited = False
        self.exit_visited = False
    
    def update_corners(self, left_top:Point, width:float, heigth:float):
        self.__left = left_top.x
        self.__top = left_top.y

        self.__right = left_top.x + width
        self.__bottom = left_top.y + heigth

    def draw(self, left_top:Point, width:float, heigth:float):

        self.update_corners(left_top, width, heigth)

        if isinstance(self.__window, Window):
            
            self.draw_walls(self.__window)

    def redraw(self):

        if isinstance(self.__window, Window):
            
            self.draw_walls(self.__window)
            self.__window.redraw()
    

    def draw_wall(self, window:Window, wall:Wall):
       window.draw_cell_wall(wall.line(), wall.visible)
    
    def draw_walls(self, window:Window):
       for wall in self.__walls.values():
           self.draw_wall(window, wall)
       
    def left_wall(self) -> Line:
        return Line(self.left_bottom(), self.left_top())
    
    def right_wall(self) -> Line:
        return Line(self.right_top(), self.right_bottom())
   
    def top_wall(self) -> Line:
        return Line(self.left_top(), self.right_top())

    def bottom_wall(self) -> Line:
        return Line(self.right_bottom(), self.left_bottom())
    
    def left_top(self) -> Point:
        return Point(self.__left, self.__top)

    def right_top(self) -> Point:
        return Point(self.__right, self.__top)
    
    def left_bottom(self) -> Point:
        return Point(self.__left, self.__bottom)

    def right_bottom(self) -> Point:
        return Point(self.__right, self.__bottom)
    
    def center_point(self) -> Point:
        return self.left_top().mid_point(self.right_bottom())

    @staticmethod
    def color(gray:bool)-> str:
        return "gray" if gray else "red" 

    def draw_move(self, to_cell, undo=False):
        if isinstance(self.__window, Window):
            self.__window.draw_line(Line(self.center_point(), to_cell.center_point()), Cell.color(undo))        

    def wall(self, wall_index:WALLINDEX) -> Wall:
        return self.__walls[wall_index]
            
    def visible_walls(self) -> list[Wall]:
        return [wall for wall in self.__walls.values() if wall.visible] 

    def set_invisible(self, wall_index:WALLINDEX) -> None:
         self.__walls[wall_index].visible = False   
 
    def reset_visited(self) -> None:
        self.entrans_visited = False
        self.exit_visited = False
    
    def reset_wals(self) -> None:
        for wall in self.__walls.values():
            wall.visible = True



