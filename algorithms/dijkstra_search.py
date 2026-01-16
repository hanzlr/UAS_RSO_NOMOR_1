import heapq

def dijkstra_search(grid, start, goal):
    rows, cols = grid.shape
    pq = [(0, start)]
    dist = {start: 0}
    came_from = {}
    closed = set()

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            break

        closed.add(current)

        yield {
            "current": current,
            "open": set(n for _, n in pq),
            "closed": closed.copy()
        }

        for dy, dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny, nx = current[0]+dy, current[1]+dx
            neighbor = (ny, nx)

            if 0 <= ny < rows and 0 <= nx < cols and grid[ny, nx] == 0:
                nd = dist[current] + 1
                if nd < dist.get(neighbor, 1e9):
                    dist[neighbor] = nd
                    came_from[neighbor] = current
                    heapq.heappush(pq, (nd, neighbor))

    path = []
    cur = goal
    while cur in came_from:
        path.append(cur)
        cur = came_from[cur]
    path.append(start)
    path.reverse()

    return path
