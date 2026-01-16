import numpy as np

def rrt_path(grid, start, goal, max_iter=15000, step_size=1):
    """
    Hasil akhir path dari RRT
    """
    # jalur sama dengan rrt_search, tapi simpan semua nodes
    nodes = {start: None}
    height, width = grid.shape

    for _ in range(max_iter):
        ry = np.random.randint(0, height)
        rx = np.random.randint(0, width)
        rand_node = (ry, rx)
        nearest = min(nodes.keys(), key=lambda n: (n[0]-ry)**2 + (n[1]-rx)**2)
        dy = ry - nearest[0]
        dx = rx - nearest[1]
        dist = np.hypot(dy, dx)
        if dist == 0:
            continue
        ny = int(round(nearest[0] + dy / dist * step_size))
        nx = int(round(nearest[1] + dx / dist * step_size))
        new_node = (ny, nx)
        if ny < 0 or ny >= height or nx < 0 or nx >= width:
            continue
        if grid[ny, nx] != 0:
            continue
        if new_node in nodes:
            continue
        nodes[new_node] = nearest
        if np.hypot(new_node[0]-goal[0], new_node[1]-goal[1]) <= step_size:
            nodes[goal] = new_node
            break

    # rekonstruksi path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = nodes.get(node)
    path.reverse()
    return path
