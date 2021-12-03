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


def process_p2():
    vals = {}
    for (key, count_index, tiebreak) in (("oxygen", 0, "1"), ("co2", 1, "0")):
        input_data = [l for l in common.read_string_file()]
        debug(key)
        for i in range(len(input_data[0])):
            c = Counter()
            for l in input_data:
                c[l[i]] += 1
            mc = c.most_common(2)
            debug(mc)
            if (len(mc) > 1) and (mc[0][1] == mc[1][1]):
                keepbit = tiebreak
            else:
                keepbit = mc[count_index][0]
            input_data = [l for l in input_data if l[i] == keepbit]
            debug(f"{i=}  {c=}  {input_data=}  {keepbit=}")
            if len(input_data) == 1:
                vals[key] = int("".join(input_data[0]), 2)
                break
    debug(vals)
    return vals["oxygen"] * vals["co2"]


def part_1():
    return process_p1()


def part_2():
    return process_p2()
