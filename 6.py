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

visited = set()

def dfs(x, y):
    if x < 0 or y < 0 or x >= rows or y >= cols:
        return False

    if maze[x][y] == 1:
        return False

    if (x, y) in visited:
        return False

    print("Visited:", (x, y))

    if (x, y) == (rows - 1, cols - 1):
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


print("\nStarting DFS from (0, 0)\n")

if not dfs(0, 0):
    print("No path found!")