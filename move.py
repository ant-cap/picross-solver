
from puzzle import Puzzle
from line import Line
from segment import Segment
from clue import Clue, CLUE_SOLVED

from utility import DIAG_ERROR, DIAG_NONE, DIAG_DELETE, DIAG_SEGSOLVABLE, DIAG_LINESOLVED, \
                    CELL_EMPTY, CELL_FILLED, CELL_CROSSED

class Move:
    def __init__(self, turn):
        self.turn = turn
        self.puzzle = turn.solver.puzzle
        self.lines: list[Line] = self.puzzle.columns + self.puzzle.rows
        self.decision: int = DIAG_NONE
        self.exception: Exception = None

        self.segment: Segment = None
        self.line: Line = None
        self.DecideMove()

    def __str__(self):
        return "[DIAG: {}]".format(self.decision)

    def DecideMove(self):
        def ProposeDecision(decision: int, line: Line, segment: Segment) -> bool:
            if self.decision == DIAG_NONE or self.decision > decision:
                self.decision = decision
                self.segment = segment
                self.line = line
    
        for line in self.lines:
            if line.IsSolved():
                continue
            if CanDeleteLine(line):
                ProposeDecision(DIAG_DELETE, line, line.segments[0])
            if LineAlreadySolved(line):
                seg = Segment(0, line.cells)
                seg.add_clue(line.clues)
                ProposeDecision(DIAG_LINESOLVED, line, seg)

            for seg in line.segments:
                if CanSolveSegment(seg):
                    ProposeDecision(DIAG_SEGSOLVABLE, line, seg)
                    #break
        #print("The Decision:", self.decision)
        try:
            DoMove(self.segment, self.decision)
        except Exception as e:
            self.exception = e
            print(e)
            return
        
        #self.VerifySolvedSegments()
    
def CanDeleteLine(line: Line) -> bool:
    if line.clues[0].value == 0 and line.clues[0].state != CLUE_SOLVED:
        return True
    return False

def LineAlreadySolved(line: Line) -> bool:
    if len(line.clues) == len(line.sequences):
        for i in range(len(line.clues)):
            if line.clues[i].value != line.sequences[i].length:
                return False
        return True
    return False

def CanSolveSegment(segment: Segment) -> bool:
    if segment.solved:
        return False
    
    if len(segment.clues) == 1 and segment.clues[0].state == CLUE_SOLVED:
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

    elif decision == DIAG_LINESOLVED:
            for i in range(len(cells)):
                if cells[i].state != CELL_FILLED:
                    cells[i].SetState(CELL_CROSSED)
            assert segment.CheckSolved() == True

    elif decision == DIAG_SEGSOLVABLE:
            cell_i = 0
            for i in range(len(clues)):
                SetStates(CELL_FILLED, cell_i, cell_i + clues[i].value)
                cell_i += clues[i].value + 1
                if cell_i >= len(cells):
                    break

            assert cell_i >= len(cells)
            assert segment.CheckSolved() == True