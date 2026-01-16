from map.grid_map import grid, START, GOAL

from algorithms.astar_search import astar_search    
from algorithms.astar_path import astar_path

from algorithms.rrt_search import rrt       # generator untuk animasi
from algorithms.rrt_path import rrt_path    # final path list

from visualization.animate_search import animate_search
from visualization.animate_final_compare import animate_final_compare
from visualization.plot_final import plot_final

from evaluation.benchmark import benchmark
import time

# ===============================
# ANIMASI A* SEARCH
# ===============================
print("A* SEARCH")
animate_search(
    grid,
    astar_search(grid, START, GOAL),
    START,
    GOAL,
    "A* Search Process"
)

# ===============================
# ANIMASI RRT SEARCH
# ===============================
print("RRT SEARCH")
animate_search(
    grid,
    rrt(grid, START, GOAL),  # generator untuk animasi
    START,
    GOAL,
    "RRT Search Process"
)

# ===============================
# FINAL PATH UNTUK BENCHMARK
# ===============================
# Buat function wrapper supaya benchmark bisa rekam waktu
def compute_rrt_path(g, s, e):
    return rrt_path(g, s, e)

# ===============================
# BENCHMARK
# ===============================
print("\n=== BENCHMARK RESULTS ===")
result_astar = benchmark(astar_path, grid, START, GOAL)
result_rrt   = benchmark(compute_rrt_path, grid, START, GOAL)

print(f"A*  | Length: {result_astar['length']} | Turns: {result_astar['turns']} | Time: {result_astar['time']:.6f} s")
print(f"RRT | Length: {result_rrt['length']} | Turns: {result_rrt['turns']} | Time: {result_rrt['time']:.6f} s")

# ===============================
# FINAL PATH ANIMATION (COMPARE)
# ===============================
animate_final_compare(
    grid,
    result_astar["path"],
    result_rrt["path"],
    START,
    GOAL
)

# ===============================
# FINAL STATIC PLOT
# ===============================
plot_final(
    grid,
    result_astar["path"],
    result_rrt["path"],
    START,
    GOAL
)
