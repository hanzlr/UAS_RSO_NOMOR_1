import matplotlib.pyplot as plt
import numpy as np

def animate_search(grid, generator, start, goal, title):
    fig, ax = plt.subplots(figsize=(6, 6))
    plt.subplots_adjust(right=0.75)  # ruang legend

    # ===== MAP =====
    ax.imshow(grid, cmap="gray_r", origin="lower")
    ax.set_xlim(-0.5, grid.shape[1]-0.5)
    ax.set_ylim(-0.5, grid.shape[0]-0.5)

    # ===== START & GOAL =====
    ax.scatter(start[1], start[0], c="green", s=70, label="Start", zorder=3)
    ax.scatter(goal[1], goal[0], c="blue", s=70, label="Goal", zorder=3)

    # ===== SEARCH NODES =====
    open_sc = ax.scatter([], [], c="yellow", s=12, label="Open Set", zorder=2)
    closed_sc = ax.scatter([], [], c="purple", s=12, label="Closed Set", zorder=2)
    current_sc = ax.scatter([], [], c="red", s=50, label="Current Node", zorder=4)

    # ===== TITLE & LEGEND =====
    ax.set_title(title)
    ax.legend(
        loc="upper left",
        bbox_to_anchor=(1.02, 1),
        borderaxespad=0
    )

    # ===== GRID LINE =====
    ax.set_xticks(np.arange(-0.5, grid.shape[1], 1))
    ax.set_yticks(np.arange(-0.5, grid.shape[0], 1))
    ax.grid(color="lightgray", linestyle="-", linewidth=0.3)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    plt.show(block=False)

    # ===== ANIMASI SEARCH =====
    for state in generator:
        if "current" not in state:
            continue

        # convert ke array 
        open_nodes = np.array(list(state["open"])) if state["open"] else np.empty((0,2))
        closed_nodes = np.array(list(state["closed"])) if state["closed"] else np.empty((0,2))

        cy, cx = state["current"]

        open_sc.set_offsets(open_nodes[:, ::-1])
        closed_sc.set_offsets(closed_nodes[:, ::-1])
        current_sc.set_offsets([[cx, cy]])

        fig.canvas.draw_idle()
        plt.pause(0.03)  # kecepatan animasi

    # ===== TAHAN WINDOW =====
    plt.show()
