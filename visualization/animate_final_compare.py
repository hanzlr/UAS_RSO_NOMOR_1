import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_final_compare(grid, path_a, path_d, start, goal):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # ================= A* MAP =================
    ax1.imshow(grid, cmap="gray_r", origin="lower")
    ax1.scatter(start[1], start[0], c="green", s=80, label="Start")
    ax1.scatter(goal[1], goal[0], c="blue", s=80, label="Goal")

    # 🔴 PATH A*
    ay, ax = zip(*path_a)
    ax1.plot(ax, ay, "r-", linewidth=2, label="A* Path")

    robot_a, = ax1.plot([], [], "ro", markersize=7, label="Robot")
    ax1.set_title("Final Path A*")
    ax1.legend(loc="upper left")

    # ================= DIJKSTRA MAP =================
    ax2.imshow(grid, cmap="gray_r", origin="lower")
    ax2.scatter(start[1], start[0], c="green", s=80, label="Start")
    ax2.scatter(goal[1], goal[0], c="blue", s=80, label="Goal")

    # 🔵 PATH DIJKSTRA
    dy, dx = zip(*path_d)
    ax2.plot(dx, dy, "b-", linewidth=2, label="Dijkstra Path")

    robot_d, = ax2.plot([], [], "bo", markersize=7, label="Robot")
    ax2.set_title("Final Path Dijkstra")
    ax2.legend(loc="upper left")

    max_len = max(len(path_a), len(path_d))

    def init():
        y, x = path_a[0]
        robot_a.set_data([x], [y])

        y, x = path_d[0]
        robot_d.set_data([x], [y])

        return robot_a, robot_d

    def update(frame):
        if frame < len(path_a):
            y, x = path_a[frame]
            robot_a.set_data([x], [y])

        if frame < len(path_d):
            y, x = path_d[frame]
            robot_d.set_data([x], [y])

        return robot_a, robot_d

    anim = animation.FuncAnimation(
        fig,
        update,
        frames=max_len,
        init_func=init,
        interval=80,
        blit=True
    )

    plt.tight_layout()
    plt.show()
