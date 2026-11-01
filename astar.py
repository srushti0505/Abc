import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def heuristic(state):
    distance = 0

    for i, value in enumerate(state):
        if value != 0:
            goal_index = GOAL.index(value)

            distance += abs(i // 3 - goal_index // 3)
            distance += abs(i % 3 - goal_index % 3)

    return distance


def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = zero // 3, zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            new_state = list(state)

            new_state[zero], new_state[new_zero] = (
                new_state[new_zero], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def a_star(start):
    priority_queue = []
    heapq.heappush(priority_queue, (heuristic(start), 0, start))

    parent = {start: None}
    cost = {start: 0}

    while priority_queue:
        f, g, current = heapq.heappop(priority_queue)

        if g != cost[current]:
            continue

        if current == GOAL:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for neighbor in get_neighbors(current):
            new_cost = g + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = current

                h = heuristic(neighbor)
                heapq.heappush(
                    priority_queue,
                    (new_cost + h, new_cost, neighbor)
                )

    return None


def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])
    print()


print("Enter the initial puzzle (use 0 for blank):")

start = []

for i in range(3):
    row = list(map(int, input().split()))
    start.extend(row)

start = tuple(start)

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input! Enter numbers 0 to 8 exactly once.")
else:
    solution = a_star(start)

    if solution:
        print("\nSolution found!")
        print("Number of moves:", len(solution) - 1)

        for step, state in enumerate(solution):
            print("Step", step)
            print_state(state)
    else:
        print("No solution exists.")