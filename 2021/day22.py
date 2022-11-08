import common
from common import debug
import settings

import attr


class BadRange(Exception):
    pass


@attr.define
class Instruction:
    position: bool
    x_range: tuple = ()
    y_range: tuple = ()
    z_range: tuple = ()

    def set_range(self, axis, minval, maxval, limit=None):
        if limit is not None:
            if minval > limit:
                raise BadRange
            if maxval < -limit:
                raise BadRange
            if minval < -limit:
                minval = -limit
            if maxval > limit:
                maxval = limit
            if (maxval - minval) < 0:
                raise BadRange
        setattr(self, f"{axis}_range", range(minval, maxval + 1))

    def get_points(self):
        points = {}
        for x in self.x_range:
            for y in self.y_range:
                for z in self.z_range:
                    points[(x, y, z)] = self.position
        debug(points)
        return points


def get_instructions(limit):
    input_data = common.read_string_file()

    for l in input_data:
        (position, range_strings) = l.split(" ")
        ranges = []
        inst = Instruction(position == "on")
        try:
            for range_string in range_strings.split(","):
                inst.set_range(
                    range_string[0],
                    *[int(i) for i in range_string[2:].split("..")],
                    limit=limit,
                )
        except BadRange:
            continue
        yield inst


def process(limit):
    points = {}
    for instruction in get_instructions(limit):
        debug(instruction)
        points.update(instruction.get_points())
    return sum([p for p in points.values() if p])


def part_1():
    return process(limit=50)


def part_2():
    return process()
