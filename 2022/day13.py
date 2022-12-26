import common
from common import debug
import settings

from collections import namedtuple
from itertools import zip_longest

NO_RESULT = "No Result"
CORRECT = "Correct"
INCORRECT = "Incorrect"


def process():
    with open(settings.settings.input_file, "r") as fh:
        for line in fh:
            l = line.strip()
            if not l:
                pair = []
            else:
                pair.append(eval(line.strip()))
            if len(pair) == 2:
                yield pair


def is_list(obj):
    return hasattr(obj, "append")


def compare_lists(left, right):
    debug(f"{left=} {right=}")
    result = NO_RESULT
    for (l, r) in zip_longest(left, right, fillvalue=None):
        debug(f"{l=} {r=}")
        if not is_list(l) and not is_list(r):
            # 2 ints, compare
            if l == r:
                continue
            if l < r:
                result = CORRECT
            if r < l:
                result = INCORRECT
            break
    return result


def part_1():
    for (n, pair) in enumerate(process(), 1):
        result = compare_lists(*pair)
        debug(f"{n=} {result=}")
        debug("")
    return ""


def part_2():
    return process()
