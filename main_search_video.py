from map.grid_map import grid, START, GOAL

from algorithms.astar_search import astar_search
from algorithms.dijkstra_search import dijkstra_search
from algorithms.astar_path import astar_path
from algorithms.dijkstra_path import dijkstra_path

from visualization.animate_all_to_video import animate_all_to_video


# SEARCH GENERATOR
astar_gen = astar_search(grid, START, GOAL)
dijk_gen  = dijkstra_search(grid, START, GOAL)

# FINAL PATH
path_a = astar_path(grid, START, GOAL)
path_d = dijkstra_path(grid, START, GOAL)

# EXPORT VIDEO
animate_all_to_video(
    grid,
    astar_gen,
    dijk_gen,
    path_a,
    path_d,
    START,
    GOAL,
    filename="Astar_vs_Dijkstra.mp4"
)
