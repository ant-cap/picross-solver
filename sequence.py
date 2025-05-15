from cell import Cell, CELL_FILLED

'''
Defines a sequence of filled cells on a line.
    index  : what cell index the sequence starts on
    cells  : the cells of the sequence
'''
class Sequence:
    def __init__(self, index, cells):
        self.start: int = index
        self.length: int = len(cells)
        self.end: int = index + self.length
        self.cells: list[Cell] = cells

    def __str__(self):
        return "{} at {}".format(self.length, self.index)
    
def GenerateSequences(cells: list[Cell]) -> list[Sequence]:
        sequences = []
        i = 0
        while i < len(cells):
            if cells[i].state is CELL_FILLED:
                length = 0
                j = i
                while cells[j].state is CELL_FILLED:
                    length += 1
                    j += 1
                    if j >= len(cells):
                        break
                sequences.append(Sequence(i, cells[i:j]))
                i = j
            else:
                i += 1
        return sequences