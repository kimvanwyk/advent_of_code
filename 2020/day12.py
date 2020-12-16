import common
from common import debug
import settings


def process_instructions(instructions, facing=90):
    location = [0, 0]

    # in format (location index, multiplier)
    directions = {
        0: (1, 1),
        90: (0, 1),
        180: (1, -1),
        270: (0, -1),
    }
    degrees = {"N": 0, "E": 90, "S": 180, "W": 270}
    for instruction in instructions:
        action = instruction[0]
        steps = int(instruction[1:])
        debug((instruction, action, steps))

        if action == "F":
            (d, mult) = directions[facing]
            location[d] += mult * steps
        if action in degrees:
            (d, mult) = directions[degrees[action]]
            location[d] += mult * steps
        if action in ("L", "R"):
            mult = 1 if action == "R" else -1
            facing += mult * steps
            if facing < 0:
                facing += 360
            if facing >= 360:
                facing -= 360
    return location


def process():
    input_data = common.read_string_file()
    return input_data


def part_1():
    instructions = process()
    (x, y) = process_instructions(instructions)
    dist = abs(x) + abs(y)
    debug((x, y, dist))
    return dist


def part_2():
    return process()
