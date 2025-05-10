from clue import Clue, CLUE_PARTIAL, CLUE_SOLVED
from cell     import Cell, CELL_FILLED
from sequence import Sequence

class Segment:
    def __init__(self, cells):
        self.solved: bool = False
        self.cells: list[Cell] = cells
        self.clues: list[Clue] = []
        self.sequences: list[Sequence] = self.GenerateSequences()

    def __str__(self):
        return "{} Clues: {}".format(self.cells, self.clues)

    def GenerateSequences(self):
        sequences = []
        cells = self.cells
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
                sequences.append(Sequence(i, length))
                i = j
            else:
                i += 1
        return sequences
        
    def add_clue(self, clue: Clue | list[Clue]):
        if isinstance(clue, Clue):
            self.clues.append(clue)
        else:
            for c in clue:
                self.clues.append(c)
        self.clues = list(set(self.clues))
    
    def CheckSolved(self) -> bool:
        clues = self.clues
        seqs = self.GenerateSequences()
        if not len(self.clues):
            return False
        if len(clues) == 1 and len(seqs) == 1:
            if clues[0].value == seqs[0].length:
                self.solved = True
                clues[0].state = CLUE_SOLVED
                return True
        return False