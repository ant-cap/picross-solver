from utility import CELL_EMPTY, CELL_FILLED, CELL_CROSSED, style

'''
Defines a cell on the grid.
    state    : current state of the cell. (empty, filled, crossed)
    position : x/y position of the cell on the grid.
'''
class Cell:
    def __init__(self, x: int = 0, y: int = 0, state: int = CELL_EMPTY):
        self.state: int = state
        self.changedState: bool = False

    def __str__(self):
        s = style.BLUE if self.changedState else style.RESET
        if self.state == CELL_EMPTY:
            s += "_"
        elif self.state == CELL_FILLED:
            s += "█"
        else:
            s += "X"
        self.changedState = False
        return s + style.RESET
        
    def __repr__(self):
        return self.__str__()
    
    def SetState(self, state: int):
        if self.state == state:
            return
        self.state = state
        self.changedState = True