import common
from common import debug
import settings


class Points:
    def __init__(self):
        input_data = common.read_string_file()
        self.points = {}
        for (y, line) in enumerate(input_data, 1):
            for (x, val) in enumerate(f".{line}."):
                self.points[(x, y, 0)] = val == "#"
                self.points[(x, y, -1)] = False
                self.points[(x, y, 1)] = False
        # Add start and end lines in all z's
        for z in (-1, 0, 1):
            for x in range(len(line) + 2):
                self.points[x, 0, z] = False
                self.points[x, y + 1, z] = False
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


# def apply_rules(points):
#     for point in points:


def part_1():
    points = Points()
    points.show()
    return ""


def part_2():
    return process()
