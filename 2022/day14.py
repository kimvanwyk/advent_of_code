import common
from common import debug
import settings

from point2d import Point2D
from rich import print


def point_repr(self):
    return f"Point({self.x}, {self.y})"


Point2D.__repr__ = point_repr


def process():
    points = {}
    for l in common.read_string_file():
        row_points = [Point2D(*[int(c) for c in p.split(",")]) for p in l.split(" -> ")]
        debug(row_points)
        for row_idx in range(1, len(row_points)):
            diff = row_points[row_idx] - row_points[row_idx - 1]
            if diff.x:
                step = Point2D(-1 if diff.x < 0 else 1, 0)
            else:
                step = Point2D(0, -1 if diff.y < 0 else 1)
            current = row_points[row_idx - 1]
            points[current] = "r"
            while (current.x, current.y) != (
                row_points[row_idx].x,
                row_points[row_idx].y,
            ):
                current += step
                debug(current)
                points[current] = "r"
            debug(f"{row_points[row_idx - 1]=} {row_points[row_idx]=} {diff=} {step=}")
    debug(points)
    return ""


def part_1():
    return process()


def part_2():
    return process()
