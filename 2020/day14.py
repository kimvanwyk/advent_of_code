from bitarray import bitarray
import bitarray.util as bt_util

import common
from common import debug
import settings


class Mask:
    def __init__(self):
        self.and_mask = bitarray(endian="big")
        self.or_mask = bitarray(endian="big")
        self.and_map = {"X": 1, "1": 1, "0": 0}
        self.or_map = {"X": 0, "1": 1, "0": 0}

    def update(self, mask):
        self.and_mask.clear()
        self.or_mask.clear()
        for c in mask:
            self.and_mask.append(self.and_map[c])
            self.or_mask.append(self.or_map[c])
        debug(f"Mask: {mask}")
        debug(f"& Mask: {self.and_mask}")
        debug(f"| Mask: {self.or_mask}")

    def apply(self, val):
        bt = bt_util.int2ba(val, length=36, endian="big")
        debug(f"Input:  {bt}")
        bt &= self.and_mask
        bt |= self.or_mask
        debug(f"Masked: {bt}")
        return bt_util.ba2int(bt)


def process():
    input_data = common.read_string_file()
    return input_data


def part_1():
    mask = Mask()
    memory = {}
    for line in process():
        if "mask" in line:
            mask.update(line.split("=")[-1].strip())
        elif "mem" in line:
            (m, data) = line.split("=")
            address = int(m.split("[")[-1].split("]")[0])
            val = mask.apply(int(data.strip()))
            debug(f"Setting address {address:08} to {val}")
            memory[address] = val
    return sum(memory.values())


def part_2():
    return process()
