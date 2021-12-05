import common
from common import debug
import settings


def process():
    input_data = common.read_string_file()
    straight = []
    for line in input_data:
        debug(line)
        points = [
            [int(p) for p in point.strip().split(",")] for point in line.split("->")
        ]
        for (fixed_pos, var_pos) in ((0, 1), (1, 0)):
            increment = [None, None]
            if points[0][fixed_pos] == points[1][fixed_pos]:
                difference = points[1][var_pos] - points[0][var_pos]
                increment[fixed_pos] = 0
                increment[var_pos] = difference // abs(difference)
                points.append(increment)
                straight.append(points)
                debug(straight[-1])
                break
    return ""


def part_1():
    return process()


def part_2():
    return process()
