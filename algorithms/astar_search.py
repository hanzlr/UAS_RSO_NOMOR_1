import heapq

def manhattan(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar_search(grid, start, goal):
    rows, cols = grid.shape
    open_set = []
    heapq.heappush(open_set, (0, start))
    g = {start: 0}
    closed = set()

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            break

        closed.add(current)

        yield {
            "current": current,
            "open": set(n for _, n in open_set),
            "closed": closed.copy()
        }

        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = current[0]+dy, current[1]+dx
            n = (ny, nx)

            if 0 <= ny < rows and 0 <= nx < cols and grid[ny, nx] == 0:
                if n in closed:
                    continue
                ng = g[current] + 1
                if ng < g.get(n, 1e9):
                    g[n] = ng
                    f = ng + manhattan(n, goal)
                    heapq.heappush(open_set, (f, n))
