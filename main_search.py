from map.grid_map import grid, START, GOAL

from algorithms.astar_search import astar_search
from algorithms.dijkstra_search import dijkstra_search
from algorithms.astar_path import astar_path
from algorithms.dijkstra_path import dijkstra_path

from visualization.animate_search import animate_search
from visualization.animate_final_compare import animate_final_compare
from visualization.plot_final import plot_final

from evaluation.benchmark import benchmark


# ===============================
# A* SEARCH ANIMATION
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
# DIJKSTRA SEARCH ANIMATION
# ===============================
print("DIJKSTRA SEARCH")
animate_search(
    grid,
    dijkstra_search(grid, START, GOAL),
    START,
    GOAL,
    "Dijkstra Search Process"
)

# ===============================
# BENCHMARK
# ===============================
print("\n=== BENCHMARK RESULTS ===")

result_astar = benchmark(astar_path, grid, START, GOAL)
result_dijk  = benchmark(dijkstra_path, grid, START, GOAL)

print(f"A*        | Length: {result_astar['length']}"
      f" | Turns: {result_astar['turns']}"
      f" | Time: {result_astar['time']:.6f} s")

print(f"Dijkstra  | Length: {result_dijk['length']}"
      f" | Turns: {result_dijk['turns']}"
      f" | Time: {result_dijk['time']:.6f} s")

# ===============================
# FINAL PATH ANIMATION (COMPARE)
# ===============================
animate_final_compare(
    grid,
    result_astar["path"],
    result_dijk["path"],
    START,
    GOAL
)

# ===============================
# FINAL STATIC PLOT
# ===============================
plot_final(
    grid,
    result_astar["path"],
    result_dijk["path"],
    START,
    GOAL
)
