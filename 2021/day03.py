from collections import Counter

import common
from common import debug
import settings


def process_p1():
    input_data = common.read_string_file()
    bits = []
    for line in input_data:
        debug(line)
        for (n, bit) in enumerate(line):
            if n == len(bits):
                bits.append(Counter())
            bits[n][bit] += 1
    debug(bits)
    gamma = []
    epsilon = []
    for bc in bits:
        (most, least) = bc.most_common(2)
        gamma.append(most[0])
        epsilon.append(least[0])
    debug(f"{gamma=}  ({''.join(gamma), 2})  {epsilon=}  ({''.join(epsilon), 2})")
    return int("".join(gamma), 2) * int("".join(epsilon), 2)


def part_1():
    return process_p1()


def part_2():
    return process()
