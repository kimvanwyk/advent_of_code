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
            regions[region] = {"area": 0, "perims": 0, "points": []}
        region_map[point] = region
        regions[region]["area"] += 1
        regions[region]["perims"] += perims
        regions[region]["points"].append(point)
        # debug((point, val, region, regions[region]))
    debug([(k, v["area"], v["perims"]) for (k, v) in regions.items()])

    for letter, max_num in region_frequency.items():
        for number in range(1, max_num + 1):
            collapsed = False
            rn = f"{letter}{number:02}"
            if rn in regions:
                for other in range(1, max_num + 1):
                    ro = f"{letter}{other:02}"
                    debug(letter, max_num, number, other, rn, ro)
                    if (number != other) and (ro in regions):
                        for po in regions[ro]["points"]:
                            for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                                dp = po + Point(dx, dy)
                                if dp in regions[rn]["points"]:
                                    # regions ajoin, move to number version
                                    regions[rn]["points"].extend(regions[ro]["points"])
                                    regions[rn]["area"] += regions[ro]["area"]
                                    regions[rn]["perims"] += regions[ro]["perims"]
                                    del regions[ro]
                                    collapsed = True
                                    break
                            if collapsed:
                                break
                    if collapsed:
                        break

    debug([(k, v["area"], v["perims"]) for (k, v) in regions.items()])
    return sum(v["area"] * v["perims"] for v in regions.values())


def part_2():
    return process()
