from utility import CELL_EMPTY, CELL_FILLED, CELL_CROSSED
from line import Line

'''
Defines a cell on the grid.
    state    : current state of the cell. (empty, filled, crossed)
    position : x/y position of the cell on the grid.
'''
class Cell:
    def __init__(self, x: int = 0, y: int = 0, state: int = CELL_EMPTY):
        self.state: int = state
        
        self.row: Line = None
        self.col: Line = None

    def __str__(self):
        if self.state == CELL_EMPTY:
            return "_"
        elif self.state == CELL_FILLED:
            return "█"
        else:
            return "X" 
        
    def __repr__(self):
        return self.__str__()
    
    def SetState(self, state: int):
        if self.state == state:
            return
        self.state = state
        if self.row and self.col:
            self.row.Update()
            self.col.Update()