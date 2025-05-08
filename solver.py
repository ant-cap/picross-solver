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
        while True:
            turn = Turn(self)
            self.turns.append(turn)

            if turn.move.decision == DIAG_NONE or turn.move.decision == DIAG_ERROR:
                break

            self.puzzle.Update()

            print(self)


    def __str__(self):
        s = "    Move {}".format(len(self.turns))
        return str(self.puzzle) + s