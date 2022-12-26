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
    debug(f"{left=}")
    debug(f"{right=}")
    result = NO_RESULT
    for (l, r) in zip_longest(left, right, fillvalue=None):
        debug(f"{l=}")
        debug(f"{r=}")
        if l is None:
            # left side of list out of items
            debug("l out of items, CORRECT")
            result = CORRECT
        elif r is None:
            # right side of list out of items
            debug("r out of items, INCORRECT")
            result = INCORRECT
        elif not is_list(l) and not is_list(r):
            # 2 ints, compare
            if l == r:
                continue
            elif l < r:
                debug("l < r, CORRECT")
                result = CORRECT
            elif r < l:
                debug("l > r, INCORRECT")
                result = INCORRECT
        if result != NO_RESULT:
            return result

        if not is_list(l):
            l = [l]
        if not is_list(r):
            r = [r]
        debug(f"{l=}")
        debug(f"{r=}")

        if len(r) > 0 and len(l) == 0:
            result = CORRECT
            debug("l empty, CORRECT")
        elif len(l) > 0 and len(r) == 0:
            debug("r empty, INCORRECT")
            result = INCORRECT
        else:
            result = compare_lists(l, r)

        if result != NO_RESULT:
            return result
    return result


def part_1():
    indices = []
    for (n, pair) in enumerate(process(), 1):
        result = compare_lists(*pair)
        debug(f"{n=} {result=}")
        debug("")
        if result == CORRECT:
            indices.append(n)
    print(indices)
    return sum(indices)


def part_2():
    return process()
