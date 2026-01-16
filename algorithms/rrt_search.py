# rrt_search.py
import numpy as np
import random

# ===============================
# Helper Functions
# ===============================

def distance(a, b):
    """Euclidean distance"""
    return np.linalg.norm(np.array(a) - np.array(b))

def is_free(grid, node):
    """Check if node is inside grid and free (0)"""
    y, x = node
    ROWS, COLS = grid.shape
    return 0 <= y < ROWS and 0 <= x < COLS and grid[y, x] == 0

def line_free(grid, p1, p2):
    """Check if straight line from p1 to p2 is free"""
    y1, x1 = p1
    y2, x2 = p2
    dy = y2 - y1
    dx = x2 - x1
    steps = int(max(abs(dy), abs(dx)))
    if steps == 0:
        return True
    for i in range(steps + 1):
        y = int(round(y1 + dy * i / steps))
        x = int(round(x1 + dx * i / steps))
        if not is_free(grid, (y, x)):
            return False
    return True

def get_random_node(grid, goal=None, goal_bias=0.1):
    """Random node with goal bias"""
    ROWS, COLS = grid.shape
    if goal and random.random() < goal_bias:
        return goal
    return (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))

# ===============================
# RRT Generator for Animation
# ===============================

def rrt(grid, start, goal, max_iter=5000, step_size=1, goal_bias=0.1):
    """
    RRT generator for animation
    Yields dict {"open": set, "closed": set, "current": node, "parent": node}
    """
    tree = {start: None}  # node -> parent
    open_set = set([start])
    closed_set = set()

    for _ in range(max_iter):
        rand_node = get_random_node(grid, goal, goal_bias)
        
        # find nearest node in tree
        nearest = min(tree.keys(), key=lambda n: distance(n, rand_node))
        
        # move towards rand_node by step_size
        vec = np.array(rand_node) - np.array(nearest)
        norm = np.linalg.norm(vec)
        if norm == 0:
            new_node = nearest
        else:
            vec = vec / norm
            new_node = tuple(np.round(np.array(nearest) + vec * step_size).astype(int))
        
        # check if new_node is valid
        if not is_free(grid, new_node) or not line_free(grid, nearest, new_node):
            # yield tetap agar animasi tidak berhenti
            yield {"open": open_set, "closed": closed_set, "current": nearest, "parent": tree[nearest]}
            continue
        
        # add new_node
        tree[new_node] = nearest
        open_set.add(new_node)
        closed_set.add(nearest)
        
        yield {"open": open_set, "closed": closed_set, "current": new_node, "parent": nearest}
        
        # check if goal reached
        if distance(new_node, goal) <= step_size and line_free(grid, new_node, goal):
            tree[goal] = new_node
            yield {"open": open_set, "closed": closed_set, "current": goal, "parent": new_node}
            break
    
    return tree

# ===============================
# RRT Final Path Extraction
# ===============================

def rrt_path(grid, start, goal, max_iter=5000, step_size=3, goal_bias=0.1):
    """
    Returns list of path nodes from start to goal
    """
    # buat generator dulu
    gen = rrt(grid, start, goal, max_iter, step_size, goal_bias)
    
    tree = {}
    last_node = None
    for state in gen:
        if "current" in state:
            node = state["current"]
            parent = state.get("parent", None)
            tree[node] = parent
            last_node = node
    
    # goal tidak tercapai
    if goal not in tree:
        return []
    
    # reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = tree.get(node)
    path.reverse()
    return path
