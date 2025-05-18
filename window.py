from tkinter import Tk, Canvas

class Window:
    def __init__(self, width:int, height:int) -> None:
        self.__root = Tk()
        self.__root.title("maze_solver")
        self.__root.minsize(width, height)
        
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        
        self.__is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()       
        self.__canvas
        self.is_running = True

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    @staticmethod
    def create_and_run_window(width:int, height:int):
        win = Window(width, height)
        win.wait_for_close()    

if __name__ == '__main__':
    Window.create_and_run_window(400,400)

    