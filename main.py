from puzzle import Puzzle
from solver import Solver
from database import Database

def main():
    puz = Puzzle()
    solver = Solver(puz)
    db = Database()

    db.Load5x5Puzzles()

if __name__ == "__main__":
    main()