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
        # debug(f"{l=} {r=}")
        if not is_list(l) and not is_list(r):
            # 2 ints, compare
            if l is None:
                # left side of list out of items
                result = CORRECT
            elif r is None:
                # right side of list out of items
                result = INCORRECT
            elif l == r:
                continue
            elif l < r:
                result = CORRECT
            elif r < l:
                result = INCORRECT
            if result != NO_RESULT:
                break

        if not is_list(l):
            l = [l]
        if not is_list(r):
            r = [r]

        if len(r) > 0 and len(l) == 0:
            result = CORRECT
        elif len(l) > 0 and len(r) == 0:
            result = INCORRECT
        else:
            result = compare_lists(l, r)

        if result != NO_RESULT:
            break
    return result


def part_1():
    correct_sum = 0
    for (n, pair) in enumerate(process(), 1):
        result = compare_lists(*pair)
        debug(f"{n=} {result=}")
        debug("")
        if result == CORRECT:
            correct_sum += n
    return correct_sum


def part_2():
    return process()
