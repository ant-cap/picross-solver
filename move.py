
from puzzle import Puzzle
from line import Line
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
        def ProposeDecision(decision: int, line: Line):
            if self.decision == DIAG_NONE:
                self.decision = decision
                self.line = line
            elif self.decision > decision:
                self.decision = decision
                self.line = line
    
        for line in self.lines:
            try:
                if self.CanDelete(line):
                    ProposeDecision(DIAG_DELETE, line)
                    break
            except Exception as e:
                self.exception = e
                self.decision = DIAG_ERROR
                return
            self.decision = DIAG_NONE
        try:
            DoMove(self.line, self.decision)
        except Exception as e:
            self.exception = e
            return
        
    def CanDelete(self, line: Line) -> bool:
        if not line.clues:
            return True
        if line.clues[0].value == 0 and line.clues[0].state != CLUE_SOLVED:
            return True
        return False
    
    def CanSolveSegment(self, line: Line) -> bool:
        for i in range(len(line.segments)):
            segment = line.segments[i]
            if segment.solved:
                continue
            
        
def DoMove(line: Line, decision: int):
    def Cross(start: int, stop: int = 0):
        if stop == 0:
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
    