import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate_final_path(grid, path, start, goal, title):
    fig, ax = plt.subplots(figsize=(6, 6))

    ax.imshow(grid, cmap="gray_r", origin="lower")
    ax.scatter(start[1], start[0], c="green", s=80, label="Start")
    ax.scatter(goal[1], goal[0], c="blue", s=80, label="Goal")

    # robot = titik merah
    robot, = ax.plot([], [], "ro", markersize=8, label="Robot")

    ax.set_title(title)
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 1))
    plt.tight_layout()

    def init():
        y, x = path[0]
        robot.set_data([x], [y])   # ⬅ LIST
        return robot,

    def update(frame):
        y, x = path[frame]
        robot.set_data([x], [y])   # ⬅ LIST
        return robot,

    anim = animation.FuncAnimation(
        fig,
        update,
        frames=len(path),
        init_func=init,
        interval=80,
        blit=True
    )

    plt.show()
