import heapq

def dijkstra_path(grid, start, goal):
    rows, cols = grid.shape
    pq = [(0, start)]
    came = {}
    dist = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            break

        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = current[0]+dy, current[1]+dx
            n = (ny, nx)
            if 0 <= ny < rows and 0 <= nx < cols and grid[ny, nx] == 0:
                nd = dist[current] + 1
                if nd < dist.get(n, 1e9):
                    dist[n] = nd
                    came[n] = current
                    heapq.heappush(pq, (nd, n))

    path = []
    cur = goal
    while cur in came:
        path.append(cur)
        cur = came[cur]
    path.append(start)
    return path[::-1]
