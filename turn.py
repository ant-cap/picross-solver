from solver import Solver
from move import Move

class Turn:
    def __init__(self, solver: Solver):
        self.solver = solver
        self.move = Move(self)
        
        