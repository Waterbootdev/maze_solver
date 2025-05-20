import unittest
from maze import Maze

class _Maze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        self.assertEqual(
            len(m1.__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.__cells[0]),
            num_rows,
        )
    
    def test_maze_cells_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_cols, num_rows, 10, 10)
        bools = [] 
        for col in m1.__cells:
            for cell in col:
                bools.append(cell.entrans_visited)
                bools.append(cell.exit_visited)
        self.assertFalse(True in bools)

if __name__ == "__main__":
    unittest.main()