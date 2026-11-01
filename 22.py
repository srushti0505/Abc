class ModelBasedAgent:
    def __init__(self, start, goal):
        self.pos = start
        self.goal = goal
        self.known_cells = {}
        self.visited = {start}
        self.path = [start]

    # Observe neighboring cells
    def sense(self, grid):
        r, c = self.pos

        neighbours = {
            "Up": (r - 1, c),
            "Down": (r + 1, c),
            "Left": (r, c - 1),
            "Right": (r, c + 1)
        }

        percepts = {}

        for direction, (nr, nc) in neighbours.items():
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                if grid[nr][nc] == 0:
                    percepts[(nr, nc)] = "Free"
                else:
                    percepts[(nr, nc)] = "Obstacle"

        return percepts

    # Update internal state
    def update_model(self, percepts):
        self.known_cells.update(percepts)

    # Choose an unvisited free cell
    def choose_action(self):
        r, c = self.pos

        moves = [
            ("Down", (r + 1, c)),
            ("Right", (r, c + 1)),
            ("Up", (r - 1, c)),
            ("Left", (r, c - 1))
        ]

        for action, cell in moves:
            if (self.known_cells.get(cell) == "Free"
                    and cell not in self.visited):
                return action, cell

        return "Backtrack", None

    # Perform one action
    def step(self, grid):
        percepts = self.sense(grid)
        self.update_model(percepts)

        if self.pos == self.goal:
            return "Goal reached"

        action, next_cell = self.choose_action()

        if next_cell is not None:
            self.pos = next_cell
            self.visited.add(next_cell)
            self.path.append(next_cell)
            return action

        # Backtrack to the previous position
        if len(self.path) > 1:
            self.path.pop()
            self.pos = self.path[-1]
            return "Backtrack"

        return "No path found"


# Take grid input from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter grid values: 0 = Free, 1 = Obstacle")

for i in range(rows):
    while True:
        row = list(map(int, input(f"Row {i + 1}: ").split()))

        if len(row) == cols and all(x in (0, 1) for x in row):
            grid.append(row)
            break

        print("Invalid input! Enter", cols, "values (0 or 1).")

# Input start and goal
start = tuple(map(int, input("Enter start (row col): ").split()))
goal = tuple(map(int, input("Enter goal (row col): ").split()))

def valid(pos):
    r, c = pos
    return (0 <= r < rows and 0 <= c < cols
            and grid[r][c] == 0)

if not valid(start) or not valid(goal):
    print("Invalid start or goal position!")
else:
    agent = ModelBasedAgent(start, goal)

    while True:
        if agent.pos == agent.goal:
            print("Goal reached!")
            break

        result = agent.step(grid)
        print("Action:", result, "| Position:", agent.pos)
  
        if result == "No path found":
            print("Goal cannot be reached.")
            break

    print("Final Path:", agent.path)
    print("Visited Cells:", agent.visited)

    print("\nGrid Environment:")
    for row in grid:
        print(" ".join(map(str, row)))