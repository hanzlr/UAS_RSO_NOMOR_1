import heapq

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar_path(grid, start, goal):
    rows, cols = grid.shape
    open_set = []
    heapq.heappush(open_set, (0, start))
    came = {}
    g = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            break

        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = current[0]+dy, current[1]+dx
            n = (ny, nx)
            if 0 <= ny < rows and 0 <= nx < cols and grid[ny, nx] == 0:
                ng = g[current] + 1
                if ng < g.get(n, 1e9):
                    g[n] = ng
                    came[n] = current
                    heapq.heappush(open_set, (ng + manhattan(n, goal), n))

    path = []
    cur = goal
    while cur in came:
        path.append(cur)
        cur = came[cur]
    path.append(start)
    return path[::-1]
