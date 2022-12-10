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


def process():
    for line in common.read_string_file():
        (direction, distance) = line.split(" ")
        yield (direction, int(distance))


def part_1():
    visited = defaultdict(int)
    head = Point2D(10000, 10000)
    tail = Point2D(10000, 10000)
    for (direction, distance) in process():
        debug(f"{direction=}  {distance=}")
        for step in range(distance):
            head += DIRECTIONS[direction]
            diff = head - tail
            # if diff.r is 1.0, no action, head and tail are touching
            if diff.r == 2.0:
                # tail is a compass point away from head, move in suitable direction
                tail += DIRECTIONS[direction]
            elif diff.r > 2.0:
                # tail is angled away from head, make a 1 step diagonal move
                change = Point2D(*[int(math.copysign(1, p)) for p in diff.ints()])
                debug(f"{change=}")
                tail += change
            debug(f"{head.ints()=} {tail.ints()=} {diff.ints()=} {diff.r=}")
            visited[tail.ints()] += 1
    return len(visited)


def part_2():
    return process()
