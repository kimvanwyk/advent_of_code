import common
from common import debug
import settings

import inspect

START = None
END = None
POINTS = {}
LOWEST_STEPS = None


def process():
    global POINTS
    y = -1
    input_data = common.read_string_file()
    for line in input_data:
        x = -1
        y += 1
        for c in line:
            x += 1
            if c == "S":
                val = "a"
                global START
                START = (x, y)
            elif c == "E":
                val = "z"
                global END
                END = (x, y)
            else:
                val = c
            POINTS[(x, y)] = val


def process_point(current_point, steps, seen):
    steps += 1
    seen.append(current_point)
    if current_point == END:
        global LOWEST_STEPS
        if (LOWEST_STEPS is None) or (LOWEST_STEPS > steps):
            LOWEST_STEPS = steps
        return
    curval = POINTS[current_point]
    (x, y) = current_point
    for (dx, dy) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new = (x + dx, y + dy)
        debug(
            f"{str(inspect.currentframe())[10:18]} {current_point=} {curval=} {new=} {steps=}"
        )
        if (
            (new in POINTS)
            and (ord(POINTS[new]) < (ord(curval) + 2))
            and (new not in seen)
        ):
            debug(
                f"processing {curval=} {POINTS[new]=}  {ord(POINTS[new])}= {ord(curval)=}"
            )
            process_point(new, steps, seen)
    return


def part_1():
    process()
    debug(f"{START=}  {END=}  {POINTS=}")
    process_point((0, 0), 0, [])
    return LOWEST_STEPS


def part_2():
    return process()
