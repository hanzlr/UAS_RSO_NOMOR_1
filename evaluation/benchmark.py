# evaluation/benchmark.py

import time
from evaluation.metrics import path_length, count_turns


def benchmark(planner_func, grid, start, goal):
    t0 = time.time()
    path = planner_func(grid, start, goal)
    elapsed = time.time() - t0

    return {
        "path": path,
        "length": path_length(path),
        "turns": count_turns(path),
        "time": elapsed
    }
