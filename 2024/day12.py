import common
from common import debug, Point
import settings

from rich import print

from collections import defaultdict


def process():
    nodes = {}
    y = 0
    for l in common.read_string_file():
        if l:
            y += 1
            for x, c in enumerate(l, 1):
                if c != ".":
                    nodes[Point(x, y)] = c
    return (nodes, Point(1, 1), Point(x, y))


def part_1():
    (nodes, min_p, max_p) = process()
    debug((nodes, min_p, max_p))
    regions = defaultdict(list)
    region_frequency = defaultdict(int)
    region_map = {}
    for point, val in nodes.items():
        in_region = False
        perims = 0
        for dx, dy in ((-1, 0), (0, -1)):
            dp = point + Point(dx, dy)
            if not dp.in_bounds(min_p, max_p):
                perims += 1
            else:
                if nodes[dp] == val:
                    if not in_region:
                        in_region = True
                        region = region_map[dp]
                else:
                    # not in region, increase both sides perim val
                    regions[region_map[dp]]["perims"] += 1
                    perims += 1
        # check for right and bottom map edges
        for dx, dy in ((1, 0), (0, 1)):
            dp = point + Point(dx, dy)
            if not dp.in_bounds(min_p, max_p):
                perims += 1
        if not in_region:
            region_frequency[val] += 1
            region = f"{val}{region_frequency[val]:02}"
            regions[region] = {"area": 0, "perims": 0}
        region_map[point] = region
        regions[region]["area"] += 1
        regions[region]["perims"] += perims
        # debug((point, val, region, regions[region]))
    debug(regions)
    return


def part_2():
    return process()
