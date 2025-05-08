from puzzle import Puzzle

class Database:
    def __init__(self):
        self.tables = {}

        _Load5x5Puzzles(self)

    def __getitem__(self, key):
        return self.tables[key]

def _Load5x5Puzzles(db: Database):
    file = "./puzzles/5x5.txt"
    fp = open(file, 'r')

    l = []
    count = 3
    dx = 0
    dy = 0
    cluesx = []
    cluesy = []
    linesx = []
    linesy = []

    while True:
        g = []
        while count != 0:
            line = fp.readline()
            if not line:
                break
            if count == 3:
                g.append(line.strip())
            else:
                c = [l.split(" ") for l in line.strip().split(',')]
                for r in c:
                    for i in range(len(r)):
                        r[i] = int(r[i])
                g.append(c)
            count -= 1
        if not g:
            break
        l.append(g)
        fp.readline()
        count = 3

    puzzles = []
    for p in l:
        if p:
            puzzles.append(Puzzle(p))

    db.tables['5x5'] = puzzles


    # coffee cup
    # 3,3,3,1,2
    # 0,5,3 1,3,0

    # clues 3, 3, 3, 1, 2, 0, 5, 3 1, 3, 0
    # dx len(line1)
    # dy len(line2)
    # lines 1 for each clue
    # cells 1 for each cell duh
    
