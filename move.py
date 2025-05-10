
from puzzle import Puzzle
from line import Line
from segment import Segment
from clue import Clue, CLUE_SOLVED

from utility import DIAG_ERROR, DIAG_NONE, DIAG_DELETE, DIAG_SOLVABLE, \
                    CELL_EMPTY, CELL_FILLED, CELL_CROSSED

class Move:
    def __init__(self, turn):
        self.turn = turn
        self.puzzle = turn.solver.puzzle
        self.lines: list[Line] = self.puzzle.columns + self.puzzle.rows
        self.decision: int = DIAG_NONE
        self.exception: Exception = None

        self.line = None

        self.DecideMove()

    def DecideMove(self):
        def ProposeDecision(decision: int, line: Line) -> bool:
            if self.decision == DIAG_NONE or self.decision > decision:
                self.decision = decision
                self.line = line
                return True
            return False
    
        for line in self.lines:
            if CanDeleteLine(line):
                if ProposeDecision(DIAG_DELETE, line):
                    break
            for seg in line.segments:
                if CanSolveSegment(seg):
                    #if ProposeDecision(DIAG_)
                    pass
                
            self.decision = DIAG_NONE
        try:
            DoMove(self.line, self.decision)
        except Exception as e:
            self.exception = e
            return
        
        #self.VerifySolvedSegments()
    
def CanDeleteLine(line: Line) -> bool:
    if not line.clues:
        return True
    if line.clues[0].value == 0 and line.clues[0].state != CLUE_SOLVED:
        return True
    return False

def CanSolveSegment(segment: Segment) -> bool:
    if segment.solved:
        return False
    clues  = segment.clues
    length = len(segment.cells)
    tally  = 0
    for i in range(len(clues)):
        tally += clues[i].value + 1
    tally -= 1
    if tally == length:
        return True

def DoMove(line: Line, decision: int):
    def Cross(start: int, stop: int = None):
        if not stop:
            for i in range(start, len(line.cells)):
                line.cells[i].SetState(CELL_CROSSED)
            return
        for i in range(start, stop):
            line.cells[i].SetState(CELL_CROSSED)

    if decision == DIAG_ERROR or decision == DIAG_NONE:
        return
    if decision == DIAG_DELETE:
        if line.clues[0].value == 0:
            Cross(0)