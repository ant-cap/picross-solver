from utility import CELL_EMPTY, CELL_FILLED, CELL_CROSSED

'''
Defines a cell on the grid.
    state    : current state of the cell. (empty, filled, crossed)
    position : x/y position of the cell on the grid.
'''
class Cell:
    def __init__(self):
        self.state = CELL_EMPTY
        