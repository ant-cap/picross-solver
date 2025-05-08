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
        while True:
            turn = Turn(self)
            self.turns.append(turn)

            print(self)
            if turn.move.decision == DIAG_NONE or turn.move.decision == DIAG_ERROR:
                break


    def __str__(self):
        s = "    Move {}".format(len(self.moves))
        return str(self.puzzle) + s