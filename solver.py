from puzzle import Puzzle
from turn import Turn

from utility import (
    DIAG_NONE, DIAG_ERROR
)

class Solver:
    def __init__(self, puzzle: Puzzle):
        self.puzzle: Puzzle = puzzle
        self.turns: list[Turn] = []

    def Execute(self):
        print(str(self.puzzle) + "    Initial Puzzle")
        i = 0
        while i < 5:
        #while True:
            turn = Turn(self)
            self.turns.append(turn)

            if turn.move.decision == DIAG_NONE or turn.move.decision == DIAG_ERROR:
                break

            self.puzzle.Update(turn.move.line)

            print(self)

            i += 1


    def __str__(self):
        s = "    Move {} {}".format(len(self.turns), self.turns[-1])
        return str(self.puzzle) + s