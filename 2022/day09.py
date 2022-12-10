import common
from common import debug
import settings

from point2d import Point2D

from collections import defaultdict
import math

DIRECTIONS = {
    "U": Point2D(0, 1),
    "D": Point2D(0, -1),
    "L": Point2D(-1, 0),
    "R": Point2D(1, 0),
}


def process(num_points):
    visited = defaultdict(int)
    points = {}
    for k in range(num_points):
        points[k] = Point2D(10000, 10000)
    for line in common.read_string_file():
        for (direction, distance) in [line.split(" ")]:
            debug(f"{direction=}  {distance=}")
            for step in range(int(distance)):
                points[0] += DIRECTIONS[direction]
                for n in range(1, len(points)):
                    diff = points[n - 1] - points[n]
                    # if diff.r is 1.0, no action, head and tail are touching
                    if diff.r == 2.0:
                        # tail is a compass point away from head, move in suitable direction
                        points[n] += DIRECTIONS[direction]
                    elif diff.r > 2.0:
                        # tail is angled away from head, make a 1 step diagonal move
                        change = Point2D(
                            *[int(math.copysign(1, p)) for p in diff.ints()]
                        )
                        debug(f"{change=}")
                        points[n] += change
                    debug(
                        f"{points[0].ints()=} {points[n].ints()=} {diff.ints()=} {diff.r=}"
                    )
                visited[points[len(points) - 1].ints()] += 1
    return len(visited)


def part_1():
    return process(2)


def part_2():
    return process()
