from clue import Clue, CLUE_UNSOLVED, CLUE_PARTIAL, CLUE_SOLVED
from cell import Cell, CELL_EMPTY, CELL_FILLED, CELL_CROSSED
from segment import Segment
from span import Span

class Line:
    def __init__(self, cells: list[Cell], clues: list[Clue]):
        self.cells: list[Cell] = cells
        self.clues: list[Clue] = clues
        self.segments: list[Segment] = [Segment(cells)]
        self.AssignClues()
        self.spans: list[Span] = self.GenerateSpans()

    def __str__(self):
        st = ""
        for s in self.segments:
            st += str(s)
        return str(self.clues) + st

    def __repr__(self):
        return self.__str__()
    
    def GenerateSpans(self) -> list[Span]:
        clues = self.clues
        cclues = [clue for clue in clues]
        cells = self.cells
        if len(clues) == 1:
            return [Span(clues[0], cells)]
        li = clues[0].value + 1
        ri = len(cells) - 1 - clues[-1].value

        first = Span(cclues.pop(0), cells[: clues[0].value + 1])
        last = Span(cclues.pop(), cells[ri : len(cells) - 1])

        #for i in range(len(cclues)):


        spans = [first]


        spans.append(last)
        return spans


    def GenerateSegments(self) -> list[Segment]:
        segments = []
        cells = self.cells
        i = 0
        while cells[i].state == CELL_CROSSED:
            i += 1
            if i >= len(cells):
                return segments
        while i < len(cells):
            segcells = []
            while cells[i].state != CELL_CROSSED:
                segcells.append(cells[i])
                i += 1
                if i >= len(cells):
                    break
            segments.append(Segment(segcells))
            if i < len(cells):
                while cells[i].state == CELL_CROSSED:
                    i += 1
                    if i >= len(cells):
                        return segments
        return segments

    def AssignClues(self) -> None:
        def WalkSegments(reverse: bool = False):
            segments = [segment for segment in self.segments]
            clues = [clue for clue in self.clues]
            assignments = [[] for segment in segments]
            if reverse:
                clues.reverse()
                segments.reverse()
            for i in range(len(segments)):
                length = len(segments[i].cells)
                tally = 0
                for j in range(len(clues)):
                    clue = clues[j]
                    tally += clue.value
                if tally > length:
                    for k in range(j):
                        assignments[i].append(clues.pop(0))
                    break
                if length - tally == 1:
                    tally += 1
                if length == tally:
                    for k in range(j+1):
                        assignments[i].append(clues.pop(0))
                    break
                if length > tally:
                    for j in range(len(clues)):
                        assignments[i].append(clues.pop(0))
            if reverse:
                assignments.reverse()
            return assignments

        segments = self.segments
        if not segments:
            if not self.clues or self.clues[0].value == 0:
                self.clues[0].state = CLUE_SOLVED
                return
            #print("wtf.")
            return
        if len(segments) == 1:
            print("segment:", segments[0])
            segments[0].add_clue(self.clues)
        else:
            ftob = WalkSegments(segments)
            btof = WalkSegments(segments, reverse=True)
            final = [[] for segment in segments]
            for i in range(len(segments)):
                for j in range(len(ftob[i])):
                    if ftob[i][j] in btof[i]:
                        final[i].append(ftob[i][j])
            for i in range(len(segments)):
                segments[i].add_clue(final[i])
        for i in range(len(segments)):
            #segments.
            pass
        self.segments = segments

    def Update(self):
        self.segments = self.GenerateSegments()
        self.AssignClues()

