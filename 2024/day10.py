import common
from common import debug, Point
import settings

from attrs import define
from rich import print


def process():
    points = {}
    zeroes = []
    for y, l in enumerate(common.read_string_file(), 1):
        for x, c in enumerate(l, 1):
            p = Point(x, y)
            points[p] = "." if c == "." else int(c)
            if points[p] == 0:
                zeroes.append(p)
    return (zeroes, points, Point(x, y))


def process_point(point, points, min_point, max_point, found, seen):
    for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        dp = point + Point(dx, dy)
        if (dp.in_bounds(min_point, max_point)) and (points[dp] != "."):
            dv = points[dp]
            v = points[point]
            debug(f"{seen=} {found=} {dx=} {dy=} {point=} {dp=} {v=} {dv=}")
            if dv == v + 1:
                if dv == 9:
                    seen[dp] = 1
                    debug("found")
                    debug("")
                    return found + 1
                else:
                    found = process_point(dp, points, min_point, max_point, found, seen)
    return found


def part_1():
    (zeroes, points, max_point) = process()
    found = 0
    for z in zeroes:
        debug(f"{z=}")
        seen = {}
        f = process_point(z, points, Point(1, 1), max_point, 0, seen)
        debug(f"found: {f}")
        debug(f"num seen: {len(seen)}")
        found += len(seen)
    return found


def part_2():
    return process()
