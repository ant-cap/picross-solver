class Database:
    def __init__(self):
        self.tables = {}

    def Load5x5Puzzles(self):
        
        l = []

        file = "./puzzles/5x5.txt"
        fp = open(file, 'r')
        
        count = 3
        done = False
        while not done:
            p = []
            while count != 0:
                line = fp.readline()
                if not line:
                    done = True
                    break
                if count == 3:
                    p.append(line.strip())
                else:
                    c = [l.split(" ") for l in line.strip().split(',')]
                    for r in c:
                        for i in range(len(r)):
                            r[i] = int(r[i])
                    p.append(c)
                count -= 1
            l.append(p)
            fp.readline()
            count = 3

        print(l)
        self.tables['5x5'] = l

