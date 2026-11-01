class ModelBasedAgent:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.pos = start
        self.goal = goal
        self.known_cells = {start: "Free"}
        self.visited = {start}
        self.parent = {start: None}
        self.rows = len(grid)
        self.cols = len(grid[0])

    def sense(self):
        r, c = self.pos
        neighbours = [(r+1,c), (r,c+1), (r-1,c), (r,c-1)]
        percepts = {}

        for nr, nc in neighbours:
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] == 0:
                    percepts[(nr,nc)] = "Free"
                else:
                    percepts[(nr,nc)] = "Obstacle"

        return percepts

    def find_path(self):
        stack = [self.pos]

        while stack:
            self.pos = stack[-1]

            if self.pos == self.goal:
                break

            self.known_cells.update(self.sense())
            r, c = self.pos
            neighbours = [(r+1,c), (r,c+1), (r-1,c), (r,c-1)]

            moved = False

            for cell in neighbours:
                if self.known_cells.get(cell) == "Free" and cell not in self.visited:
                    self.visited.add(cell)
                    self.parent[cell] = self.pos
                    stack.append(cell)
                    moved = True
                    break

            if not moved:
                stack.pop()

        if not stack:
            return None

        path = []
        current = self.goal

        while current is not None:
            path.append(current)
            current = self.parent[current]

        return path[::-1]

    def run(self):
        path = self.find_path()

        if path is None:
            print("Goal cannot be reached.")
            return

        print("Goal reached!")
        print("Path:", path)
        print("Number of moves:", len(path) - 1)
        print("Visited cells:", self.visited)
        print("Known cells:", self.known_cells)

        display = [row[:] for row in self.grid]

        for r, c in path:
            if (r, c) != start and (r, c) != goal:
                display[r][c] = "*"

        display[start[0]][start[1]] = "S"
        display[goal[0]][goal[1]] = "G"

        print("Grid with path:")
        for row in display:
            print(" ".join(map(str, row)))


# Input grid
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []

print("Enter grid values: 0 = Free, 1 = Obstacle")

for i in range(rows):
    grid.append(list(map(int, input().split())))

start = tuple(map(int, input("Enter start (row col): ").split()))
goal = tuple(map(int, input("Enter goal (row col): ").split()))

print("Original Grid:")
for row in grid:
    print(" ".join(map(str, row)))

agent = ModelBasedAgent(grid, start, goal)
agent.run()