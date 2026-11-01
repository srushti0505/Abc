
from collections import deque

def bfs_path(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    queue = deque([start])
    parent = {start: None}

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
  
        if (r, c) == goal:
            path = []
            current = (r, c)

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for dr, dc in moves:
            nr, nc = r + dr, c + dc

            if (0 <= nr < rows and 0 <= nc < cols
                and grid[nr][nc] == 0
                and (nr, nc) not in parent):

                parent[(nr, nc)] = (r, c)
                queue.append((nr, nc))

    return None


# Take input from the user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter grid values (0 = Free, 1 = Obstacle):")

for i in range(rows):
    row = list(map(int, input(f"Enter row {i}: ").split()))

    while len(row) != cols or any(x not in (0, 1) for x in row):
        print("Invalid input! Enter exactly", cols, "values (0 or 1).")
        row = list(map(int, input(f"Enter row {i}: ").split()))

    grid.append(row)

print("\nEnter starting position:")
start_r = int(input("Start row: "))
start_c = int(input("Start column: "))
start = (start_r, start_c)

print("\nEnter goal position:")
goal_r = int(input("Goal row: "))
goal_c = int(input("Goal column: "))
goal = (goal_r, goal_c)

# Validate start and goal
if not (0 <= start_r < rows and 0 <= start_c < cols
        and 0 <= goal_r < rows and 0 <= goal_c < cols):
    print("Invalid start or goal position!")

elif grid[start_r][start_c] == 1 or grid[goal_r][goal_c] == 1:
    print("Start and goal must be free cells (0)!")

else:
    path = bfs_path(grid, start, goal)

    if path:
        print("\nPath found:", path)
        print("Steps:", len(path) - 1)
    else:
        print("No path exists")
