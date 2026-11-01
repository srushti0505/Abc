
# Maze Solving using DFS
# 0 = Open Path
# 1 = Wall

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

maze = []

print("Enter maze row by row (0 = Open, 1 = Wall):")

for i in range(rows):
    row = list(map(int, input().split()))
    maze.append(row)

start_x = int(input("Enter starting row: "))
start_y =int(input("Enter starting column: "))
goal_x = int(input("Enter goal row: "))
goal_y = int(input("Enter goal column: "))

visited = set()

def dfs(x, y):
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return False

    if maze[x][y] == 1:
        return False

    if (x, y) in visited:
        return False

    print("Visited:", (x, y))

    if (x, y) == (goal_x, goal_y):
        print("\nGoal Reached!")
        return True

    visited.add((x, y))

    if dfs(x + 1, y):
        return True

    if dfs(x - 1, y):
        return True

    if dfs(x, y + 1):
        return True

    if dfs(x, y - 1):
        return True

    return False


if (0 <= start_x < rows and
    0 <= start_y < cols and
    maze[start_x][start_y] == 0 and
    0 <= goal_x < rows and
    0 <= goal_y < cols and
    maze[goal_x][goal_y] == 0):

    print("\nStarting DFS...\n")

    if not dfs(start_x, start_y):
        print("\nNo path found!")

else:
    print("Invalid start or goal position!")
