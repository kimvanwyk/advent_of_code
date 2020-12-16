import common
from common import debug
import settings


def parse_instruction(instruction):
    action = instruction[0]
    steps = int(instruction[1:])
    debug((instruction, action, steps))
    return (action, steps)


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
        (action, steps) = parse_instruction(instruction)

        if action == "F":
            (d, mult) = directions[facing]
            location[d] += mult * steps
        if action in degrees:
            (d, mult) = directions[degrees[action]]
            location[d] += mult * steps
        if action in ("L", "R"):
            if action == "L":
                steps = 360 - steps
            facing += steps
            if facing >= 360:
                facing -= 360
    return location


def process_waypoint_instructions(instructions, waypoint=[10, 1]):
    location = [0, 0]
    # in format (waypoint index, multiplier)
    directions = {
        0: (1, 1),
        90: (0, 1),
        180: (1, -1),
        270: (0, -1),
    }
    degrees = {"N": 0, "E": 90, "S": 180, "W": 270}
    for instruction in instructions:
        (action, steps) = parse_instruction(instruction)
        if action == "F":
            direction = [w * steps for w in waypoint]
            for (n, (l, d)) in enumerate(zip(location, direction)):
                location[n] = l + d
        if action in degrees:
            (d, mult) = directions[degrees[action]]
            waypoint[d] += mult * steps
        if action in ("L", "R"):
            wpx = waypoint[0]
            wpy = waypoint[1]
            for s in range(((360 - steps) if action == "L" else steps) // 90):
                (wpx, wpy) = (wpy, -1 * wpx)
            waypoint = [wpx, wpy]

        debug((action, steps, location, waypoint))
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
    instructions = process()
    (x, y) = process_waypoint_instructions(instructions)
    dist = abs(x) + abs(y)
    debug((x, y, dist))
    return dist
