# Borrowing cube setting approach from https://github.com/Dullstar/Advent_Of_Code/blob/main/python/year2021/day22.py

import common
from common import debug
import settings

import attr


@attr.define
class Point:
    x: int
    y: int
    z: int

    def add_1(self):
        self.x += 1
        self.y += 1
        self.z += 1


@attr.define
class Cuboid:
    p1: Point
    p2: Point
    volume: int = 0
    is_valid: bool = None

    def __attrs_post_init__(self):
        vols = [getattr(self.p2, p) - getattr(self.p1, p) for p in ("x", "y", "z")]
        v = 1
        for vol in vols:
            v *= vol
        self.volume = v
        self.is_valid = all(
            [getattr(self.p1, p) < getattr(self.p2, p) for p in ("x", "y", "z")]
        )


@attr.define
class Instruction:
    position: bool
    cuboid: Cuboid


def get_overlap(a: Cuboid, b: Cuboid):
    # As per source code:
    # I'm not sure about a good way to explain where this formula comes from other than to draw it out with squares
    # (it'll extend out to 3 dimensions trivially), but if we do this process, and we get a cuboid that fits the
    # format that Cuboid.is_valid() expects in order for it to return True, then it's the cuboid that describes where
    # the overlap occurs, while if it returns False, then that tells us there's no overlap and we can safely discard
    # the cuboid we found.
    overlap = Cuboid(
        Point(max(a.p1.x, b.p1.x), max(a.p1.y, b.p1.y), max(a.p1.z, b.p1.z)),
        Point(min(a.p2.x, b.p2.x), min(a.p2.y, b.p2.y), min(a.p2.z, b.p2.z)),
    )
    return overlap if overlap.is_valid else None


def get_instructions(mask_cuboid=None):
    input_data = common.read_string_file()

    instructions = []
    for l in input_data:
        points = []
        (position, point_strings) = l.split(" ")
        for point_string in point_strings.split(","):
            points.append([int(i) for i in point_string[2:].split("..")])
        instructions.append(
            Instruction(
                position == "on",
                Cuboid(
                    Point(*[point[0] for point in points]),
                    Point(*[point[1] + 1 for point in points]),
                ),
            )
        )
    if mask_cuboid:
        masked = []
        for inst in instructions:
            overlap = get_overlap(inst.cuboid, mask_cuboid)
            if overlap:
                masked.append(overlap)
        return masked
    return instructions


def part_1():
    instructions = get_instructions(
        mask_cuboid=Cuboid(Point(-50, -50, -50), Point(51, 51, 51))
    )
    debug(instructions)
    return ""


def part_2():
    return ""
