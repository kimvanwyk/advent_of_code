from collections import namedtuple

import common
from common import debug
import settings

Point = namedtuple("Point", ("x", "y", "z"))


class Points:
    def __init__(self):
        input_data = common.read_string_file()
        self.points = {}
        for (y, line) in enumerate(input_data, 1):
            for (x, val) in enumerate(f".{line}."):
                self.points[Point(x, y, 0)] = val == "#"
                self.points[Point(x, y, -1)] = False
                self.points[Point(x, y, 1)] = False
        # Add start and end lines in all z's
        for z in (-1, 0, 1):
            for x in range(len(line) + 2):
                self.points[Point(x, 0, z)] = False
                self.points[Point(x, y + 1, z)] = False
        self.mins = {"x": 0, "y": 0, "z": -1}
        self.maxs = {"x": len(line) + 1, "y": y + 1, "z": 1}

    def show(self):
        for z in range(self.mins["z"], self.maxs["z"] + 1):
            print("z = ", z)
            for y in range(self.mins["y"], self.maxs["y"] + 1):
                out = []
                for x in range(self.mins["x"], self.maxs["x"] + 1):
                    out.append("#" if self.points.get((x, y, z), False) else ".")
                print("".join(out))
            print()
        print("-----------------------------------------------------------------")

    def loop_negihbours(self, k):
        for x in (k.x - 1, k.x, k.x + 1):
            for y in (k.y - 1, k.y, k.y + 1):
                for z in (k.z - 1, k.z, k.z + 1):
                    yield (Point(x, y, z))

    def apply_rules(self):
        current_points = list(self.points.keys())
        for k in current_points:
            active_neighbours = 0
            v = self.points[k]
            for point in self.loop_negihbours(k):
                if point != k:
                    val = self.points.get(point, None)
                    if val is None:
                        self.points[point] = False
                        for d in ("x", "y", "z"):
                            p = getattr(point, d)
                            if self.mins[d] > p:
                                self.mins[d] = p
                            elif self.maxs[d] < p:
                                self.maxs[d] = p
                    elif val:
                        active_neighbours += 1
            print(k, active_neighbours)
            if v and active_neighbours not in (2, 3):
                self.points[k] = False
            if not v and active_neighbours == 3:
                self.points[k] = True


def part_1():
    points = Points()
    points.show()
    points.apply_rules()
    points.show()
    return ""


def part_2():
    return process()
