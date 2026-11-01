
class ModelBasedAgent:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.pos = start
        self.goal = goal

        self.known_cells = {start: "Free"}
        self.visited = {start}
        self.parent = {start: None}
        self.path = []

        self.rows = len(grid)
        self.cols = len(grid[0])

    # Observe neighboring cells
    def sense(self):
        r, c = self.pos

        neighbours = [
            (r + 1, c),  # Down
            (r, c + 1),  # Right
            (r - 1, c),  # Up
            (r, c - 1)   # Left
        ]

        percepts = {}

        for nr, nc in neighbours:
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] == 0:
                    percepts[(nr, nc)] = "Free"
                else:
                    percepts[(nr, nc)] = "Obstacle"

        return percepts

    # Update the internal model
    def update_model(self, percepts):
        self.known_cells.update(percepts)

    # Find a path using DFS and backtracking
    def find_path(self):
        stack = [self.pos]

        while stack:
            self.pos = stack[-1]

            if self.pos == self.goal:
                break

            percepts = self.sense()
            self.update_model(percepts)

            r, c = self.pos
            neighbours = [
                (r + 1, c),
                (r, c + 1),
                (r - 1, c),
                (r, c - 1)
            ]

            moved = False

            for cell in neighbours:
                if (self.known_cells.get(cell) == "Free"
                        and cell not in self.visited):

                    self.visited.add(cell)
                    self.parent[cell] = self.pos
                    stack.append(cell)
                    moved = True
                    break

            if not moved:
                stack.pop()

        if not stack:
            return None

        # Reconstruct the path from goal to start
        current = self.goal

        while current is not None:
            self.path.append(current)
            current = self.parent[current]

        self.path.reverse()
        return self.path

    # Run the agent and display results
    def run(self):
        result = self.find_path()

        if result is None:
            print("\nGoal cannot be reached.")
            print("Visited cells:", self.visited)
            return

        print("\nGoal reached!")
        print("Path:", self.path)
        print("Number of moves:", len(self.path) - 1)
        print("Visited cells:", self.visited)
        print("Known cells:", self.known_cells)

        display = [row[:] for row in self.grid]

        for r, c in self.path:
            if (r, c) != start and (r, c) != goal:
                display[r][c] = "*"

        display[start[0]][start[1]] = "S"
        display[goal[0]][goal[1]] = "G"

        print("\nGrid with path:")
        for row in display:
            print(" ".join(map(str, row)))


# Take grid dimensions
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

if rows <= 0 or cols <= 0:
    print("Invalid grid dimensions!")

else:
    grid = []
    valid_grid = True

    print("Enter grid values: 0 = Free, 1 = Obstacle")

    for i in range(rows):
        while True:
            try:
                row = list(map(
                    int, input(f"Row {i + 1}: ").split()
                ))

                if len(row) == cols and all(x in (0, 1) for x in row):
                    grid.append(row)
                    break

                print("Enter exactly", cols, "values (0 or 1).")

            except ValueError:
                print("Invalid input! Enter only 0 or 1.")

    try:
        start_input = list(map(
            int, input("Enter start (row col): ").split()
        ))
        goal_input = list(map(
            int, input("Enter goal (row col): ").split()
        ))

        if len(start_input) != 2 or len(goal_input) != 2:
            print("Enter exactly two coordinates for start and goal.")

        else:
            start = tuple(start_input)
            goal = tuple(goal_input)

            def valid(pos):
                r, c = pos
                return (
                    0 <= r < rows
                    and 0 <= c < cols
                    and grid[r][c] == 0
                )

            if not valid(start) or not valid(goal):
                print("Invalid start or goal position!")

            else:
                print("\nOriginal Grid:")
                for row in grid:
                    print(" ".join(map(str, row)))

                agent = ModelBasedAgent(grid, start, goal)
                agent.run()

    except ValueError:
        print("Invalid coordinates! Enter row and column numbers.")
