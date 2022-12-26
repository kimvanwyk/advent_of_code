import common
from common import debug
import settings

import inspect


def process():
    y = -1
    points = {}
    lowest = []
    input_data = common.read_string_file()
    for line in input_data:
        x = -1
        y += 1
        for c in line:
            x += 1
            if c == "S":
                val = "a"
                start = (x, y)
            elif c == "E":
                val = "z"
                end = (x, y)
            else:
                val = c
            points[(x, y)] = val
            if val == "a":
                lowest.append((x, y))
    return (start, end, points, lowest)


# BFS hint from https://medium.com/geekculture/breadth-first-search-in-python-822fb97e0775
# Adjusted to help with part 2 by going from end to start
# - advice taken from https://medium.com/@datasciencedisciple/advent-of-code-2022-day-12-335dd851e795
def shortest_path(start, end, points):
    visited = []
    queue = [[end]]
    a_path_lens = []

    while queue:
        path = queue.pop(0)
        point = path[-1]
        (x, y) = point
        curval = points[point]
        if point not in visited:
            options = []
            for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                new = (x + dx, y + dy)
                if (new in points) and (ord(points[new]) > (ord(curval) - 2)):
                    options.append(new)
            for option in options:
                new_path = list(path)
                new_path.append(option)
                queue.append(new_path)

                if points[option] == "a":
                    a_path_lens.append(len(new_path))

                if option == start:
                    return (len(new_path), a_path_lens)

            visited.append(point)

    return (0, [])


def part_1():
    (start, end, points, lowest) = process()
    debug(f"{start=}  {end=}  {points=}")
    (path_len, a_path_lens) = shortest_path(start, end, points)
    # number of steps is 1 less than items in path
    return path_len - 1


def part_2():
    (start, end, points, lowest) = process()
    debug(f"{start=}  {end=}  {points=}  {lowest=}")
    (path_len, a_path_lens) = shortest_path(start, end, points)
    # number of steps is 1 less than items in path
    return min(a_path_lens) - 1
