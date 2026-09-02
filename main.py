
from solver import Solver
from database import Database

def main(): 
    db = Database()

    puzzles = db['5x5']

    puzzle = puzzles[0]

    solver = Solver(puzzle)

    solver.Execute()

if __name__ == "__main__":
    main()
    