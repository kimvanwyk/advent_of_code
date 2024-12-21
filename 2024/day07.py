import common
from common import debug
import settings

import more_itertools
from rich import print

from collections import defaultdict
import itertools
import operator

OPS = {"+": operator.add, "*": operator.mul}


def process():
    for l in common.read_string_file():
        (k, v) = l.split(":")
        yield (int(k), [int(c) for c in v.strip().split(" ")])


def process_vals(operators, values):
    total = 0
    for test_val, vals in values:
        debug((test_val, vals))
        l = len(vals) - 1
        ops = ""
        for o in operators:
            ops += o * l
        debug(f"{ops=}")
        success = False
        for operator_set in more_itertools.distinct_permutations(ops, l):
            debug(operator_set)
            val = vals[0]
            for i, op in enumerate(operator_set, 1):
                # debug(test_val, val, op, vals[i])
                val = OPS[op](val, vals[i])
                if val > test_val:
                    break
            if val == test_val:
                success = True
                break
        if success:
            total += test_val
    return total


def part_1():
    return process_vals("*+", process())


def part_2():
    return process()
