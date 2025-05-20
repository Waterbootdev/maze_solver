from tkinter import Tk, Canvas
from line import Line


class Window:
    def __init__(self, width:int, height:int, visible_cell_wall_color:str = "black", invisible_cell_wall_color:str = "#d9d9d9") -> None:
        self.__root = Tk()
        self.__root.title("maze_solver")
        
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        
        self.__is_running = False

        self.visible_cell_wall_color = visible_cell_wall_color
        self.invisible_cell_wall_color = invisible_cell_wall_color
    
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()       
        self.is_running = True

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False
        
    def draw_line(self, line:Line, fill_color:str):
        line.draw(self.__canvas, fill_color)
    
    def wall_color(self, visible:bool):
        return self.visible_cell_wall_color if visible else self.invisible_cell_wall_color
    
    def draw_cell_wall(self, line:Line, visible:bool):
        self.draw_line(line, self.wall_color(visible))