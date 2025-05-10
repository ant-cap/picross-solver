
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

        self.segment = None
        self.DecideMove()

    def __str__(self):
        return "[DIAG: {}]".format(self.decision)

    def DecideMove(self):
        def ProposeDecision(decision: int, segment: Segment) -> bool:
            if self.decision == DIAG_NONE or self.decision > decision:
                self.decision = decision
                self.segment = segment
    
        for line in self.lines:
            #print("line:", line)
            if CanDeleteLine(line):
                ProposeDecision(DIAG_DELETE, line.segments[0])
                #break
            for seg in line.segments:
                if CanSolveSegment(seg):
                    ProposeDecision(DIAG_SOLVABLE, seg)
                    #break
        #print("The Decision:", self.decision)
        try:
            DoMove(self.segment, self.decision)
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
    return False

def DoMove(segment: Segment, decision: int):
    def SetStates(state: int, start: int, stop: int = None):
        if not stop:
            for i in range(start, len(segment.cells)):
                segment.cells[i].SetState(state)
            return
        for i in range(start, stop):
            segment.cells[i].SetState(state)

    if decision == DIAG_ERROR or decision == DIAG_NONE:
        return
    
    cells = segment.cells
    clues = segment.clues
    if decision == DIAG_DELETE:
        if clues[0].value == 0:
            SetStates(CELL_CROSSED, 0)
    elif decision == DIAG_SOLVABLE:
        cell_i = 0
        for i in range(len(clues)):
            SetStates(CELL_FILLED, cell_i, cell_i + clues[i].value)
            cell_i += clues[i].value + 1
            if cell_i >= len(cells):
                break
        assert cell_i >= len(cells)