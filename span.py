
from clue import Clue
from cell import Cell

# Describes a range of cell indexes that could hold a clue sequence

class Span:
    def __init__(self, clue, cells):
        self.clue: Clue = clue
        self.cells: list[Cell] = cells
        