
class ModelBasedAgent:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.known = {start: "Free"}
        self.visited = {start}
        self.parent = {start: None}

    def sense(self, pos):
        r, c = pos
        neighbours = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]

        for nr, nc in neighbours:
            if 0 <= nr < len(self.grid) and 0 <= nc < len(self.grid[0]):
                if self.grid[nr][nc] == 0:
                    self.known[(nr, nc)] = "Free"
                else:
                    self.known[(nr, nc)] = "Obstacle"

    def find_path(self):
        stack = [self.start]

        while stack:
            current = stack[-1]

            if current == self.goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = self.parent[current]
                return path[::-1]

            self.sense(current)

            r, c = current
            neighbours = [(r+1, c), (r, c+1), (r-1, c), (r, c-1)]

            moved = False

            for cell in neighbours:
                if (self.known.get(cell) == "Free"
                        and cell not in self.visited):
                    self.visited.add(cell)
                    self.parent[cell] = current
                    stack.append(cell)
                    moved = True
                    break

            if not moved:
                stack.pop()

        return None


# User input
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter grid values (0 = Free, 1 = Obstacle):")

for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    grid.append(row)

start = tuple(map(int, input("Enter start (row col): ").split()))
goal = tuple(map(int, input("Enter goal (row col): ").split()))

# Create agent
agent = ModelBasedAgent(grid, start, goal)

# Find path
path = agent.find_path()

# Display result
if path is not None:
    print("\nGoal reached!")
    print("Path:", path)
    print("Number of moves:", len(path) - 1)
else:
    print("\nGoal cannot be reached.")

print("Visited cells:", agent.visited)
print("Known cells:", agent.known)
