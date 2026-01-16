# evaluation/metrics.py

def path_length(path):
    return len(path)


def count_turns(path):
    turns = 0
    for i in range(2, len(path)):
        y1, x1 = path[i-2]
        y2, x2 = path[i-1]
        y3, x3 = path[i]

        dir1 = (y2 - y1, x2 - x1)
        dir2 = (y3 - y2, x3 - x2)

        if dir1 != dir2:
            turns += 1

    return turns
