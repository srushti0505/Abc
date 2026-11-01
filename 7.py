def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


def print_board(solution):
    n = len(solution)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)
    print()   


n = int(input("Enter the value of N: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    solutions = solve_n_queens(n)

    print("Total solutions found:", len(solutions))

    if len(solutions) > 0:
        print("\nFirst solution:")
        print_board(solutions[0])
    else:
        print("No solution exists.")