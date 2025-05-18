#from window import Window
from point import Point
from line import Line

class Cell:
    def __init__(self, window) -> None:
        
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        
        self.__left = -1
        self.__top = -1
        self.__right = -1
        self.__bottom = -1

        self.__window = window
    
    def update_corners(self, left_top:Point, width:float, heigth:float):
        self.__left = left_top.x
        self.__top = left_top.y

        self.__right = left_top.x + width
        self.__bottom = left_top.y + heigth

    def draw(self, left_top:Point, width:float, heigth:float):

        self.update_corners(left_top, width, heigth)

        if self.has_top_wall:
            self.__window.draw_cell_wall(self.top_wall())

        if self.has_right_wall:
            self.__window.draw_cell_wall(self.right_wall())

        if self.has_bottom_wall:
            self.__window.draw_cell_wall(self.bottom_wall())
        
        if self.has_left_wall:
            self.__window.draw_cell_wall(self.left_wall())

        
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
        self.__window.draw_line(Line(self.center_point(), to_cell.center_point()), Cell.color(undo))        
        
    
