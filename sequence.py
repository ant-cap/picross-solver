'''
Defines a sequence of filled cells on a line.
    index  : what cell index the sequence starts on
    length : the length of the sequence 
'''
class Sequence:
    def __init__(self, index, length):
        self.index: int = index
        self.length: int = length

    def __str__(self):
        return "{} at {}".format(self.length, self.index)