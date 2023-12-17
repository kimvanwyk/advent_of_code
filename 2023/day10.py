import common
from common import debug
import settings

from rich import print

DIRECTIONS = {
    "up": ("|", "7", "F", "S"),
    "left": ("-", "L", "F", "S"),
    "down": ("|", "L", "J", "S"),
    "right": ("-", "J", "7", "S"),
}
MOVEMENTS = {
    "S": ("up", "left", "down", "right"),
    "|": ("up", "down"),
    "-": ("left", "right"),
    "L": ("up", "right"),
    "J": ("up", "left"),
    "7": ("left", "down"),
    "F": ("right", "down"),
}
OPPOSITE_DIRECTIONS = {"left": "right", "right": "left", "up": "down", "down": "up"}


def process():
    points = {}
    for y, l in enumerate(common.read_string_file()):
        for x, c in enumerate(l):
            points[(x, y)] = c
    debug(points)
    return points


def find_connection(points, start_point, from_dir=None):
    start_val = points[start_point]
    for dx, dy, direction in (
        (0, -1, "up"),
        (-1, 0, "left"),
        (0, 1, "down"),
        (1, 0, "right"),
    ):
        # check if this movement is possible
        if direction not in MOVEMENTS[start_val]:
            continue
        point = (start_point[0] + dx, start_point[1] + dy)
        val = points.get(point, None)
        debug(f"{start_point=}, {point=}, {direction=}, {val=}, {from_dir=}")
        if val is None:
            continue
        elif from_dir is not None and direction == OPPOSITE_DIRECTIONS[from_dir]:
            continue
        elif val in DIRECTIONS[direction]:
            debug(f"found")
            return (point, direction)
    return None


def part_1():
    points = process()
    pipe = []
    for (x, y), val in points.items():
        if val == "S":
            (start_x, start_y) = (x, y)
            point = (start_x, start_y)
            pipe.append(point)
            break
    direction = None
    while True:
        (point, direction) = find_connection(points, point, direction)
        val = points[point]
        pipe.append(point)
        if val == "S":
            break
    debug((start_x, start_y))
    debug(pipe)
    return (len(pipe[:-1]) // 2) + (len(pipe[:-1]) % 2)


def part_2():
    return process()
