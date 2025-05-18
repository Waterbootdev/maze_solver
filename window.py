from tkinter import Tk, Canvas
from line import Line
from point import Point
from cell import Cell

class Window:
    def __init__(self, width:int, height:int, cell_wall_color:str = "black") -> None:
        self.__root = Tk()
        self.__root.title("maze_solver")
        
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        
        self.__is_running = False

        self.cell_width = width / 10
        self.cell_height = height / 5

        self.cell_wall_color = cell_wall_color
    
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
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def draw_line(self, line:Line, fill_color:str):
        line.draw(self.__canvas, fill_color)
    
    def draw_cell_wall(self, line:Line):
        self.draw_line(line, self.cell_wall_color)
    

    @staticmethod
    def create_and_run_window(width:int, height:int):
        win = Window(width, height)
        win.wait_for_close()    

    @staticmethod
    def create_draw_some_lines_and_run_window(width:int, height:int):
        win = Window(width, height)

        top =  1
        left = 1
        bottom = height
        right = width

        win.draw_line(Line(Point(left, top), Point(right, bottom)), "red")
        win.draw_line(Line(Point(left, bottom),Point(right, top)), "green")
        win.draw_line(Line(Point(left, bottom/2),Point(right, bottom/2)), "blue")
        
        win.draw_line(Line(Point(left, top), Point(right, top)), "black")
        win.draw_line(Line(Point(left, bottom), Point(right, bottom)), "black")
        win.draw_line(Line(Point(left, top), Point(left, bottom)), "black")
        win.draw_line(Line(Point(right, top), Point(right, bottom)), "black")
        


        win.wait_for_close()    

    @staticmethod
    def create_draw_some_cells_and_run_window(width:int, height:int, step:int, factor:int, cell_wall_color="red"):
        
        win = Window(width, height, cell_wall_color=cell_wall_color)

        top =  1
        left = 1
        curent_height = height - 1
        curent_width = width - 1

        cell = Cell(win)

        for i in range(0,min(height, width)//2, step):
            cell.draw(Point(left + i, top + i), curent_width - factor * i, curent_height - factor * i)

        
        win.wait_for_close()    

if __name__ == '__main__':
    Window.create_draw_some_cells_and_run_window(800,800, 3, 3)

    