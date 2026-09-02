
from clue import Clue, CLUE_PARTIAL, CLUE_SOLVED
from cell     import Cell, CELL_FILLED, CELL_CROSSED
from sequence import Sequence, GenerateSequences

class Segment:
    def __init__(self, index, cells):
        self.solved: bool = False
        self.start: int = index
        self.end: int = index + len(cells)
        self.cells: list[Cell] = cells
        self.clues: list[Clue] = []
        self.sequences: list[Sequence] = []

    def __str__(self):
        return "{} Clues: {}".format(self.cells, self.clues)
        
    def add_clue(self, clue: Clue | list[Clue]):
        if isinstance(clue, Clue):
            self.clues.append(clue)
        else:
            for c in clue:
                self.clues.append(c)
        self.clues = list(set(self.clues))

    def add_sequence(self, seq: Sequence):
        self.sequences.append(seq)
    
    def CheckSolved(self) -> bool:
        clues = self.clues
        seqs = GenerateSequences(self.cells)
        if not len(self.clues):
            return False
        if len(clues) == 1 and len(seqs) == 1:
            if clues[0].value == seqs[0].length:
                self.solved = True
                clues[0].state = CLUE_SOLVED
                return True
        return False
    
def GenerateSegments(cells: list[Cell]) -> list[Segment]:
    segments = []
    i = 0
    while cells[i].state == CELL_CROSSED:
        i += 1
        if i >= len(cells):
            return segments
    while i < len(cells):
        segcells = []
        while cells[i].state != CELL_CROSSED:
            segcells.append(cells[i])
            i += 1
            if i >= len(cells):
                break
        segments.append(Segment(i, segcells))
        if i < len(cells):
            while cells[i].state == CELL_CROSSED:
                i += 1
                if i >= len(cells):
                    return segments
    return segments
    