from time import sleep
from window import Window
from cell import Cell
from wall_index import WALLINDEX, opposite
from point import Point
import random
from maze_path import MazePath, Position
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
        seed=None,
        sleep_animated:bool  = False
    ) -> None:
        self.x1 = x1
        self.y1 = y1
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.cell_size_x=cell_size_x
        self.cell_size_y=cell_size_y
        self.win = win
        self.sleep_animated = sleep_animated

        if seed is not None:
            random.seed(seed)

        self.create_and_draw(num_cols, num_rows, win)

        self.create_maze_paths()

        self.reduce_visible_walls()            

        self.reset_visited(self.__cells)

        path = self.search_path()

        print(path.length)

    def search_path(self) -> MazePath:
        entrance_path = MazePath(self.entrance_positon(), self.set_entrance_visited, self.set_entrance_invisited, self.entrance_visited, self.exit_visited)
        self.search_path_r(entrance_path, self.cell(entrance_path._position), self.exit_positon())
        return entrance_path
        
    def search_path_r(self, path:MazePath, cell:Cell, exit_position):
            neigbor_positions = self.neighbors(cell, path)

            if len(neigbor_positions) > 0:
                
                if exit_position in neigbor_positions:
                    path.append(exit_position)
                    cell.draw_move(self.cell(exit_position))
                    return True
                else:
                    for position in neigbor_positions:
                        path.append(position)
                        neighbor = self.cell(position)
                        path._set_visited(position)
                        self.draw_move(cell, neighbor)
                        if self.search_path_r(path, neighbor ,exit_position):
                            return True
                        else:
                            path.step_back()
                            path._set_invisited(position)
                            self.draw_move_back(neighbor, cell)
            else:
                return False

    def draw_move(self, cell:Cell, neighbor:Cell):
        cell.draw_move(neighbor)
        self.redraw()
    
    def draw_move_back(self, cell:Cell, neighbor:Cell):
        cell.draw_move(neighbor, undo=True)
        self.redraw()

    def neighbors(self, cell:Cell, path:MazePath) -> list[Position]:
        return [wall._neighbor for wall in cell.invisible_walls() if wall._neighbor and not path._is_visited(wall._neighbor)]
    
    def create_maze_paths(self):
        entrance_path = MazePath(self.entrance_positon(), self.set_entrance_visited, self.set_entrance_invisited, self.entrance_visited, self.exit_visited)
        exit_path = MazePath(self.exit_positon(), self.set_exit_visited, self.set_exit_invisited, self.exit_visited, self.entrance_visited)

        while not self.connect(entrance_path, exit_path):
            Maze.reset(self.__cells)
            self.__break_entrance_and_exit()

    def reduce_visible_walls(self):
        visited, unvisited = Maze.group_cells(self.__cells)

        for cell in unvisited:
            for wal in [wall for wall in cell.visible_walls() if wall._neighbor and self.cell(wall._neighbor).unvisited()]:
                wal.visible = False
            cell.redraw(redraw_window=False)
  
        for cell in visited:
            cell.redraw(redraw_window=False)

        self.redraw()

    def redraw(self):
        if self.win: 
            self.win.redraw()
        
    @staticmethod
    def group_cells(cols:list[list[Cell]])-> tuple[list[Cell], list[Cell]]:
        unvisited = []
        visited=[]
        for col in cols:
            for cell in col:
                if cell.unvisited():
                    unvisited.append(cell)
                else:
                    visited.append(cell)
        
        return visited, unvisited

    @staticmethod
    def reset(cols:list[list[Cell]]) -> None:
        for col in cols:
            for cell in col:
                cell.reset_wals()
                cell.reset_visited()
                cell.redraw() 

    @staticmethod
    def reset_visited(cols:list[list[Cell]]) -> None:
        for col in cols:
            for cell in col:
                cell.reset_visited()
    

    def connect(self, first: MazePath, second:MazePath) -> bool:
        while not (self.is_connected(first) and self.is_connected(second)):
            first_append = self.append_loop(first)
            second_append = self.append_loop(second)

            if not (first_append or second_append):
                return False

        return True
   
    
    def append_loop(self, path:MazePath) -> bool:
            appandable = True
            appended = False
            while appandable and not appended:
                appended = self.append(path)
                if not appended:
                    appandable = path.step_back()
            return appended

    
    
    def append(self, path:MazePath) -> bool:
        cell = self.cell(path._position)
        walls =[wall for wall in cell.visible_walls() if wall._neighbor and not path._is_visited(wall._neighbor)]

        if walls:
            wall = random.choice(walls)
            wall.visible = False
            neighbor_position = wall._neighbor
            neighbor_cell = self.cell(neighbor_position)
            neighbor_cell.set_invisible(opposite(wall._wall_index))
            path._set_visited(neighbor_position)
            path.append(neighbor_position)
            cell.redraw()
            neighbor_cell.redraw()
            return True
        else:
            return False

    def is_connected(self, path):
        return path._is_other_visited(path._position)
    
    def create_and_draw(self, num_cols, num_rows, win):
        self.__cells = Maze.__create_cells(win, num_cols, num_rows)

        for x, col in enumerate(self.__cells):
            for y, cell in enumerate(col):
                self.__draw_cell(cell, x, y)

        self.__break_entrance_and_exit()


    @staticmethod
    def __create_cells(win, num_cols, num_rows) -> list[list[Cell]]:
         return [Maze.__create_cols(win, num_rows, x, num_cols) for x in range(num_cols)]

    @staticmethod
    def __create_cols(win:Window, num_rows:int, x:int, num_cols:int) -> list[Cell]:
        return [Maze.__cell(win, x, num_cols, y, num_rows) for y in range(num_rows)]
    
    @staticmethod
    def __cell(win, x:int, num_cols, y:int, num_rows)-> Cell:
        cell = Cell(win)
        for wall in cell.visible_walls():
            wall._neighbor = Maze.neighbor_position(wall._wall_index, x, num_cols, y, num_rows)
        return cell

    @staticmethod       
    def neighbor_position(wall_index:WALLINDEX, x:int, num_cols, y:int, num_rows)-> Position|None:
        
        match wall_index:
            case WALLINDEX.TOP:
                y -= 1
            case WALLINDEX.BOTTOM: 
                y += 1
            case WALLINDEX.LEFT:
                x -= 1
            case WALLINDEX.RIGHT:
                x += 1

        if Maze.valid(x, num_cols) and Maze.valid(y, num_rows):
            return Position(x,y)
        else:
            return None     
    
    @staticmethod
    def valid(x:int, num)->bool:
        return x >= 0 and x < num
     
    def __draw_cell(self, cell:Cell, x:int, y:int) -> None:
        cell.draw(Point(self.x1 + x * self.cell_size_x, self.y1 + y * self.cell_size_y), self.cell_size_x, self.cell_size_y)
        
        
    def __break_entrance_and_exit(self):
        self.entrance().wall(WALLINDEX.TOP).visible = False 
        self.exit().wall(WALLINDEX.BOTTOM).visible = False
        self.entrance().redraw()
        self.exit().redraw()
 
    def exit(self) -> Cell:
        return self.__cells[-1][-1]

    def entrance(self) -> Cell:
        return self.__cells[0][0]

    def entrance_positon(self) -> Position:
        return Position(0,0)
    
    def exit_positon(self) -> Position:
        return Position(self.num_cols - 1, self.num_rows - 1)
    
    def entrance_visited(self, position:Position) -> bool:
        return self.cell(position).entrans_visited
    
    def exit_visited(self, position:Position) -> bool:
        return self.cell(position).exit_visited
    
    def set_entrance_visited(self, position:Position|None) -> None:
        if position:
            self.cell(position).entrans_visited = True
        else:
            raise Exception()
    def set_entrance_invisited(self, position:Position|None) -> None:
        if position:
            self.cell(position).entrans_visited = False
        else:
            raise Exception()
    
    def set_exit_visited(self, position:Position|None) -> None:
        if position:
            self.cell(position).exit_visited = True
        else:
            raise Exception()
    
    def set_exit_invisited(self, position:Position|None) -> None:
        if position:
            self.cell(position).exit_visited = False
        else:
            raise Exception()
    
    def cell(self, position:Position|None)-> Cell:
        if position:
            return self.__cells[position.x][position.y]
        else:
            raise Exception()
    

