from clue import Clue
from cell import Cell

class Line:
    def __init__(self, cells: list[Cell], clues: list[Clue]):
        self.cells: list[Cell] = cells
        self.clues: list[Clue] = clues

    def __str__(self):
        return str(self.clues) + str(self.cells)
    
    def __repr__(self):
        return self.__str__()
    
    def Update(self):
        pass