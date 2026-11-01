
rows=int(input("enter no of rows:"))
cols=int(input("enter no cols:"))
maze=[]

for i in range(rows):
    row=list(map(int,input().split()))
    maze.append(row)

start_r=int(input("Enter starting row"))
start_c=int(input("Enter starting col"))
goal_r=int(input("enter goal row"))
goal_c=int(input("enter goal col"))

visited=set()
path=[]

def dfs(x,y):
    if x<0 or y<0 or x>=rows or y>=cols:
        return False

    if maze[x][y]==1:
        return False

    if (x,y) in visited:
        return False

    print("visited",(x,y))
    path.append((x,y))

    if (x,y)==(goal_r,goal_c):
        print("goal reached")
        return True

    visited.add((x,y))

    if dfs(x+1,y):
        return True
    if dfs(x-1,y):
        return True
    if dfs(x,y+1):
        return True
    if dfs(x,y-1):
        return True

    path.pop()
    return False


if (0 <= start_r < rows and
    0 <= start_c < cols and
    maze[start_r][start_c] == 0 and
    0 <= goal_r < rows and
    0 <= goal_c < cols and
    maze[goal_r][goal_c] == 0):

    print("\nStarting DFS...\n")

    if dfs(start_r, start_c):
        print("Total path:",path)
        print("Total steps:",len(path)-1)
    else:
        print("\nNo path found!")

else:
    print("Invalid start or goal position!")
