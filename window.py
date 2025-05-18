from tkinter import Tk, BOTH, Canvas, YES
from line import Line
from point import Point

class Window:
    def __init__(self, width:int, height:int) -> None:
        self.__root = Tk()
        self.__root.title("maze_solver")
        
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        
        self.__is_running = False

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
        

    @staticmethod
    def create_and_run_window(width:int, height:int):
        win = Window(width, height)
        win.wait_for_close()    

    @staticmethod
    def create_draw_some_lines_and_run_window(width:int, height:int):
        win = Window(width, height)

        top =  0
        left = 0
        bottom = height
        right = width

        win.draw_line(Line(Point(left, top), Point(right, bottom)), "red")
        win.draw_line(Line(Point(left, bottom),Point(right, top)), "green")
        win.draw_line(Line(Point(left, bottom/2),Point(right, bottom/2)), "blue")
        

        win.wait_for_close()    

if __name__ == '__main__':
    Window.create_draw_some_lines_and_run_window(800,800)

    