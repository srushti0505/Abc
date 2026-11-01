
class ModelBasedAgent:
    def __init__(self, start, goal):
        self.pos = start
        self.goal = goal
        self.known = {}
        self.visited = {start}
        self.path = [start]

    def step(self, grid):
        r, c = self.pos

        if self.pos == self.goal:
            return "Goal reached"

        moves = [(r+1,c), (r,c+1), (r-1,c), (r,c-1)]

        for nr, nc in moves:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                self.known[(nr,nc)] = grid[nr][nc]

                if grid[nr][nc] == 0 and (nr,nc) not in self.visited:
                    self.pos = (nr,nc)
                    self.visited.add(self.pos)
                    self.path.append(self.pos)
                    return "Move"

        if len(self.path) > 1:
            self.path.pop()
            self.pos = self.path[-1]
            return "Backtrack"

        return "No path found"


rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

grid = []
print("Enter grid (0 = Free, 1 = Obstacle):")

for i in range(rows):
    grid.append(list(map(int, input().split())))

start = tuple(map(int, input("Enter start (row col): ").split()))
goal = tuple(map(int, input("Enter goal (row col): ").split()))

if not (0 <= start[0] < rows and 0 <= start[1] < cols
        and 0 <= goal[0] < rows and 0 <= goal[1] < cols
        and grid[start[0]][start[1]] == 0
        and grid[goal[0]][goal[1]] == 0):
    print("Invalid start or goal!")
else:
    agent = ModelBasedAgent(start, goal)

    while agent.pos != goal:
        result = agent.step(grid)
        print(result, "| Position:", agent.pos)

        if result == "No path found":
            break

    print("Final Path:", agent.path)
    print("Visited Cells:", agent.visited)
