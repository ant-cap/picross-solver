class Line:
    def __init__(self, cells, clues):
        self.cells = cells
        self.clues = clues

    def __str__(self):
        return str(self.clues) + str(self.cells)
    
    def __repr__(self):
        return self.__str__()