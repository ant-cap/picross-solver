from move import Move

class Turn:
    def __init__(self, solver):
        self.solver = solver
        self.move = Move(self)
        
    def __str__(self):
        return str(self.move)