from time import sleep
from window import Window
from cell import Cell
from point import Point
class Maze:
    def __init__(
        self,
        x1 : float,
        y1 : float,
        num_cols : int,
        num_rows : int,
        cell_size_x : float,
        cell_size_y : float,
        win = None,
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win = win
        self.__cells = Maze.__create_cells(win, num_cols, num_rows)


        for x, col in enumerate(self.__cells):
            for y, cell in enumerate(col):
                self.__draw_cell(cell, x, y)

        self.__break_entrance_and_exit()


    @staticmethod
    def __create_cells(win, num_cols, num_rows) -> list[list[Cell]]:
         return [Maze.__create_cols(win, num_rows) for _ in range(num_cols)]

    @staticmethod
    def __create_cols(win, num_rows) -> list[Cell]:
        return [Cell(win) for _ in range(num_rows)]
        
        
    def __draw_cell(self, cell:Cell, x:int, y:int) -> None:
        cell.draw(Point(self.x1 + x * self.cell_size_x, self.y1 + y * self.cell_size_y), self.cell_size_x, self.cell_size_y)
        self._animate() 
        
    def _animate(self) -> None:
        if isinstance(self.win, Window): 
            self.win.redraw()
            sleep(0.0005)
        
    def __break_entrance_and_exit(self):
        self.entrance().has_top_wall = False 
        self.exit().has_bottom_wall = False
        self.entrance().redraw()
        self.exit().redraw()
 

    def exit(self) -> Cell:
        return self.__cells[-1][-1]

    def entrance(self) -> Cell:
        return self.__cells[0][0]


