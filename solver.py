from puzzle import Puzzle

class Solver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.moves = []

    def Execute(self):
        print(self)

    def __str__(self):
        s = "    Move {}".format(len(self.moves))
        return str(self.puzzle) + s