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


class FloatingMask:
    def apply(self, mask, val):
        masks = [bt_util.int2ba(val, length=36, endian="big")]
        debug(f"Input:  {masks[-1]} ({bt_util.ba2int(masks[-1])})")
        for (n, c) in enumerate(mask):
            if c == "1":
                for m in masks:
                    m[n] = True
            if c == "X":
                new = []
                for m in masks:
                    new.append(m[:])
                    new[-1][n] = True
                    m[n] = False
                masks.extend(new)
        if settings.settings.debug:
            for (n, m) in enumerate(masks):
                print(f"Output {n}: {m} ({bt_util.ba2int(m)})")
        return [bt_util.ba2int(bt) for bt in masks]


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
    mask = FloatingMask()
    memory = {}
    for line in process():
        if "mask" in line:
            mask_pattern = line.split("=")[-1].strip()
        elif "mem" in line:
            (m, data) = line.split("=")
            val = int(data)
            address = int(m.split("[")[-1].split("]")[0])
            addresses = mask.apply(mask_pattern, int(address))
            for add in addresses:
                memory[add] = val
                debug(f"Setting address {add} to {val}")
    return sum(memory.values())
