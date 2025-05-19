from window import Window
from cell import Cell
from point import Point
from line import Line
from maze import Maze
class Create:
    @staticmethod
    def create_and_run_window(width:int, height:int):
        win = Window(width, height)
        win.wait_for_close()    

    @staticmethod
    def create_draw_some_lines_and_run_window(width:int, height:int):
        win = Window(width, height)

        top =  1
        left = 1
        bottom = height + 1
        right = width + 1

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
        
        win = Window(width, height, visible_cell_wall_color=cell_wall_color)

        top =  1
        left = 1
        curent_height = height + 2 
        curent_width = width + 2

        cell = Cell(win)

        for i in range(0,min(height, width)//2, step):
            cell.draw(Point(left + i, top + i), curent_width - factor * i, curent_height - factor * i)

        
        win.wait_for_close()    
    
    @staticmethod
    def create_draw_move_and_run_window(width:int, height:int, cell_wall_color="red", undo:bool=False):
        
        win = Window(width, height, visible_cell_wall_color=cell_wall_color)

        top =  1
        left = 1
        
        curent_height = height/2
        curent_width = width/2
    
        first_cell = Cell(win)
        first_cell.draw(Point(left, top), curent_width, curent_height/2)
      
        second_cell = Cell(win)
        second_cell.draw(Point(left + 0.75 * width, top + 0.75* height), curent_width / 2, -curent_height/2)
      
        second_cell.draw_move(first_cell, undo)

        win.wait_for_close()

    @staticmethod
    def create_draw_maze_and_run_window(width:int, height:int, num_cols, num_rows, dx, dy, cell_wall_color="red", undo:bool=False):

        win = Window(width, height, visible_cell_wall_color=cell_wall_color)

        _ = Maze(1 + dx, 1 + dy, num_cols, num_rows, (width - 2 * dx) / num_cols, (height - 2 * dy) /num_rows, win)
            
        win.wait_for_close()
