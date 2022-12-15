import common
from common import debug
import settings

import inspect

START = None
END = None
POINTS = {}
LOWEST_STEPS = None


def process():
    global POINTS
    y = -1
    input_data = common.read_string_file()
    for line in input_data:
        x = -1
        y += 1
        for c in line:
            x += 1
            if c == "S":
                val = "a"
                global START
                START = (x, y)
            elif c == "E":
                val = "z"
                global END
                END = (x, y)
            else:
                val = c
            POINTS[(x, y)] = val


# BFS hint from https://medium.com/geekculture/breadth-first-search-in-python-822fb97e0775
def shortest_path():
    visited = []
    queue = [[START]]

    while queue:
        path = queue.pop(0)
        point = path[-1]
        (x, y) = point
        curval = POINTS[point]
        if point not in visited:
            options = []
            for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new = (x + dx, y + dy)
                if (new in POINTS) and (ord(POINTS[new]) < (ord(curval) + 2)):
                    options.append(new)
            for option in options:
                new_path = list(path)
                new_path.append(option)
                queue.append(new_path)

                if option == END:
                    return new_path

            visited.append(point)

    return []


def part_1():
    process()
    debug(f"{START=}  {END=}  {POINTS=}")
    path = shortest_path()
    debug(path)
    # number of steps is 1 less than items in path
    return len(path) - 1


def part_2():
    return process()
