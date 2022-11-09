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

    def set_range(self, axis, minval, maxval, limits=None):
        if limits is not None:
            if minval > limits[1]:
                raise BadRange
            if maxval < limits[0]:
                raise BadRange
            if minval < limits[0]:
                minval = limits[0]
            if maxval > limits[1]:
                maxval = limits[1]
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


def get_instructions(limit=50):
    input_data = common.read_string_file()

    positions = []
    ranges_list = []
    for l in input_data:
        (position, range_strings) = l.split(" ")
        ranges_list.append({})
        positions.append(position == "on")
        for range_string in range_strings.split(","):
            ranges_list[-1][range_string[0]] = [
                int(i) for i in range_string[2:].split("..")
            ]
    if limit is not None:
        limits_list = ((-50, 50), (-50, 50), (-50, 50))
    # else:
    #     for (pos, ranges) in zip(positions, ranges_list):

    debug(ranges_list)
    for (pos, ranges) in zip(positions, ranges_list):
        inst = Instruction(pos)
        try:
            [
                inst.set_range(k, *v, limits)
                for (limits, (k, v)) in zip(limits_list, ranges.items())
            ]
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
