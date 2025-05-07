from utility import CLUE_UNSOLVED, CLUE_PARTIAL, CLUE_SOLVED, get_super, style

'''
Defines the tomography hints that are initially provided.
    value : the value of the clue.
    index : the index of the clue, where later indexes should appear later in the line
'''
class Clue:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.solved = CLUE_UNSOLVED
        self.sequence = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.GetStyle() + "{}{}".format(self.value, get_super(self.index)) + style.RESET
    
    def GetStyle(self):
        if self.solved == CLUE_UNSOLVED:
            return style.RED
        elif self.solved == CLUE_PARTIAL:
            return style.YELLOW
        elif self.solved == CLUE_SOLVED:
            return style.GREEN
        return style.RESET