import matplotlib.pyplot as plt

def plot_final(grid, path_a, path_d, start, goal):
    plt.figure(figsize=(6,6))
    plt.imshow(grid, cmap="gray_r", origin="lower")

    ay, ax = zip(*path_a)
    dy, dx = zip(*path_d)

    plt.plot(ax, ay, "r-", label="A* Path")
    plt.plot(dx, dy, "b--", label="DIJKSTRA Path")

    plt.scatter(start[1], start[0], c="green", s=60)
    plt.scatter(goal[1], goal[0], c="black", s=60)

    plt.legend()
    plt.title("Final Path Comparison")
    plt.show()
