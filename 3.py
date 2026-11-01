
from collections import deque
import time

# Get neighboring states
def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    row, col = idx // 3, idx % 3

    moves = {
        'Up': (-1, 0),
        'Down': (1, 0),
        'Left': (0, -1),
        'Right': (0, 1)
    }

    for move, (dr, dc) in moves.items():
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)

            new_state[idx], new_state[new_idx] = (
                new_state[new_idx], new_state[idx]
            )

            neighbors.append((move, tuple(new_state)))

    return neighbors


# Breadth-First Search
def bfs(start, goal):
    queue = deque([(start, [])])
    visited = {start}
    states_explored = 0

    while queue:
        state, path = queue.popleft()
        states_explored += 1

        if state == goal:
            return path, states_explored

        for move, neighbor in get_neighbors(state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [move]))

    return None, states_explored


# Check whether puzzle is solvable
def is_solvable(state):
    tiles = [t for t in state if t != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0


# Print puzzle as a 3x3 grid
def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


# Main program
if __name__ == "__main__":

    goal_state = (1, 2, 3,
                  4, 5, 6,
                  7, 8, 0)

    print("Enter the initial 8-puzzle state.")
    print("Enter 0 for the blank space.")

    initial_state = []

    for i in range(3):
        row = list(map(
            int,
            input(f"Enter row {i + 1} (3 numbers separated by spaces): ").split()
        ))

        if len(row) != 3:
            print("Error: Enter exactly 3 numbers per row.")
            raise SystemExit

        initial_state.extend(row)

    initial_state = tuple(initial_state)

    # Validate input
    if len(set(initial_state)) != 9 or set(initial_state) != set(range(9)):
        print("Invalid input! Use numbers 0 to 8 exactly once.")
        raise SystemExit

    print("\nInitial State:")
    print_state(initial_state)

    print("Goal State:")
    print_state(goal_state)

    if not is_solvable(initial_state):
        print("Puzzle is not solvable!")
    else:
        start_time = time.time()

        solution, explored = bfs(initial_state, goal_state)

        end_time = time.time()

        if solution is not None:
            print("Solution found!")
            print("Number of moves:", len(solution))

            if solution:
                print("Moves:", " -> ".join(solution))
            else:
                print("Already at the goal state!")

        else:
            print("No solution found.")

        print("States explored:", explored)
        print(f"Time taken: {end_time - start_time:.4f} seconds")
