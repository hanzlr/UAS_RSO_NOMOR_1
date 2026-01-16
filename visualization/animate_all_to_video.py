import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.animation import FFMpegWriter
from tqdm import tqdm  # progress bar


def animate_all_to_video(
    grid,
    astar_gen,
    dijkstra_gen,
    path_a,
    path_d,
    start,
    goal,
    filename="comparison.mp4",
    fps=20
):
    # ------------------------------
    # Figure & Subplot Layout
    # ------------------------------
    fig = plt.figure(figsize=(12, 8))

    # Atas: A* dan Dijkstra, 
    # Bawah: Final Path full width
    ax_astar = plt.subplot2grid((2, 2), (0, 0))
    ax_dijk  = plt.subplot2grid((2, 2), (0, 1))
    ax_final = plt.subplot2grid((2, 1), (1, 0), colspan=2)

    axes = [ax_astar, ax_dijk, ax_final]

    # Setup semua subplot
    for ax in axes:
        ax.imshow(grid, cmap="gray_r", origin="lower")
        ax.scatter(start[1], start[0], c="green", s=60)
        ax.scatter(goal[1], goal[0], c="blue", s=60)
        ax.set_xticks([])
        ax.set_yticks([])

    ax_astar.set_title("A* Search")
    ax_dijk.set_title("Dijkstra Search")
    ax_final.set_title("Final Path Comparison")

    # ------------------------------
    # Scatter untuk Search
    # ------------------------------
    a_open = ax_astar.scatter([], [], c="yellow", s=10)
    a_closed = ax_astar.scatter([], [], c="purple", s=10)
    a_current = ax_astar.scatter([], [], c="red", s=40)

    d_open = ax_dijk.scatter([], [], c="yellow", s=10)
    d_closed = ax_dijk.scatter([], [], c="purple", s=10)
    d_current = ax_dijk.scatter([], [], c="red", s=40)

    # ------------------------------
    # Final path plotting (static)
    # ------------------------------
    ay, axp = zip(*path_a)
    dy, dxp = zip(*path_d)

    ax_final.plot(axp, ay, 'r-', linewidth=2, label="A* Path")
    ax_final.plot(dxp, dy, 'b--', linewidth=2, label="Dijkstra Path")
    ax_final.legend(loc="upper right")

    # ------------------------------
    # Simpan state ke list (untuk animasi)
    # ------------------------------
    astar_states = list(astar_gen)
    dijk_states  = list(dijkstra_gen)
    frames = max(len(astar_states), len(dijk_states))

    # ------------------------------
    # Update function animasi
    # ------------------------------
    def update(i):
        if i < len(astar_states):
            s = astar_states[i]
            if "open" in s:
                o = np.array(list(s["open"]))
                if len(o):
                    a_open.set_offsets(o[:, ::-1])
            if "closed" in s:
                c = np.array(list(s["closed"]))
                if len(c):
                    a_closed.set_offsets(c[:, ::-1])
            if "current" in s:
                y, x = s["current"]
                a_current.set_offsets([[x, y]])

        if i < len(dijk_states):
            s = dijk_states[i]
            if "open" in s:
                o = np.array(list(s["open"]))
                if len(o):
                    d_open.set_offsets(o[:, ::-1])
            if "closed" in s:
                c = np.array(list(s["closed"]))
                if len(c):
                    d_closed.set_offsets(c[:, ::-1])
            if "current" in s:
                y, x = s["current"]
                d_current.set_offsets([[x, y]])

        return [a_open, a_closed, a_current, d_open, d_closed, d_current]

    # ------------------------------
    # Animasi
    # ------------------------------
    ani = animation.FuncAnimation(
        fig,
        update,
        frames=frames,
        interval=50,  # ms per frame
        blit=True
    )

    # ------------------------------
    # Save ke video MP4 dengan FFmpeg
    # ------------------------------
    print(f"Saving video to {filename} ...")
    writer = FFMpegWriter(fps=fps, metadata=dict(artist='Raihan'), bitrate=1800)

    for _ in tqdm(range(1), desc="Rendering video"):
        ani.save(filename, writer=writer, dpi=200)

    plt.close()
    print("Video saved successfully!")
