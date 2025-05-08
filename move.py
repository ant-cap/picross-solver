from solver import Solver
from puzzle import Puzzle
from line import Line
from turn import Turn
from clue import Clue

from utility import DIAG_ERROR, DIAG_NONE, DIAG_DELETE, DIAG_SOLVABLE, \
                    CELL_EMPTY, CELL_FILLED, CELL_CROSSED

class Move:
    def __init__(self, turn: Turn):
        self.turn = turn
        self.puzzle = turn.solver.puzzle
        self.lines: list[Line] = self.puzzle.columns + self.puzzle.rows
        self.decision: int = DIAG_NONE
        self.exception: Exception = None

        self.line = None

        self.DecideMove()

    def DecideMove(self):
        for line in self.lines:
            try:
                if self.CanDelete(line):
                    self.decision = DIAG_DELETE
                    self.line = line
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
        if line.clues[0].value == 0:
            return True
        return False
        
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
    