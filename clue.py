
from sequence import Sequence
from states import CLUE_UNSOLVED, CLUE_PARTIAL, CLUE_SOLVED
from utility import get_super, style

'''
Defines the tomography hints that are initially provided.
    value : the value of the clue.
    index : the index of the clue, where later indexes should appear later in the line
'''
class Clue:
    def __init__(self, value, index):
        self.value: int = value
        self.index: int = index
        self.state: int = CLUE_UNSOLVED
        self.sequence: Sequence = None

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.GetStyle() + "{}{}".format(self.value, get_super(self.index)) + style.RESET

    def GetStyle(self):
        if self.state == CLUE_UNSOLVED:
            return style.RED
        elif self.state == CLUE_PARTIAL:
            return style.YELLOW
        elif self.state == CLUE_SOLVED:
            return style.GREEN
        return style.RESET
        