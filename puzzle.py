from line import Line
from clue import Clue
from cell import Cell, CELL_FILLED

class Puzzle:
    def __init__(self, data):
        self.solved = False

        self.name = data[0]

        colclues = data[1]
        rowclues = data[2]

        for i in range(len(colclues)):
            for j in range(len(colclues[i])):
                colclues[i][j] = Clue(colclues[i][j], j)

        for i in range(len(rowclues)):
            for j in range(len(rowclues[i])):
                rowclues[i][j] = Clue(rowclues[i][j], j)

        self.dx = len(colclues)
        self.dy = len(rowclues)

        self.rows = []
        self.columns = []
        self.cells = []

        for x in range(self.dx):
            col = []
            for y in range(self.dy):
                cell = Cell(x, y)
                #if y == 4:
                #    cell = Cell(x, y, CELL_FILLED)
                col.append(cell)
            self.cells.append(col)
            self.columns.append(col)

        for i in range(len(self.columns[0])):
            row = []
            for j in range(len(self.columns)):
                row.append(self.columns[j][i])
            self.rows.append(row)

        for i in range(len(self.columns)):
            self.columns[i] = Line(self.columns[i], colclues[i])

        for i in range(len(self.rows)):
            self.rows[i] = Line(self.rows[i], rowclues[i])



    def __str__(self):
        cels = self.cells
        cols = self.columns
        rows = self.rows

        len_vert_clues = max(len(col.clues) for col in cols)
        len_hori_clues = max(len(row.clues) for row in rows)

        vert_clues_str = ""
        for i in range(len_vert_clues -1, -1, -1):
            vert_clues_str += "   " * len_hori_clues
            for j in range(self.dx):
                if i >= len(cols[j].clues):
                    vert_clues_str += "  "
                else:
                    vert_clues_str += str(cols[j].clues[i])
                vert_clues_str += " "
            vert_clues_str += "\n"



        hori_clues_grid_str = "\n"
        for i in range(self.dx):
            for j in range(self.dy):
                hori_clues_grid_str += str(cels[j][i]) + " "
            hori_clues_grid_str += "\n"
        return vert_clues_str + hori_clues_grid_str + self.name