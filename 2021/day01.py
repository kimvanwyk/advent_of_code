import common
from common import debug
import settings


def process_p1():
    inc = 0
    input_data = common.read_integer_file()
    first = next(input_data)
    for second in input_data:
        debug(f"{first=} {second=}")
        if second > first:
            inc += 1
        first = second
    return inc


def process_p2():
    inc = 0
    input_data = common.read_integer_file()
    windows = [[], [], []]
    # prime first 3 windows
    for n in range(3):
        val = next(input_data)
        while n >= 0:
            windows[n].append(val)
            n -= 1
    for val in input_data:
        windows.append([])
        for n in (-3, -2, -1):
            windows[n].append(val)
    debug(windows)
    sums = {0: sum(windows[0])}
    for (n, w) in enumerate(windows[1:], 1):
        if len(w) < 3:
            break
        if sums.setdefault(n, sum(w)) > sums[n - 1]:
            inc += 1
    debug(sums)
    return inc


def part_1():
    return process_p1()


def part_2():
    return process_p2()
