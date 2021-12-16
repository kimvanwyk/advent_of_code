import common
from common import debug
import settings

import math

HEX_MAPPINGS = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

PACKET_STRING = ""


class Packet:
    def __init__(self, idx):
        self.literal = False
        self.sub_bytes_type = None
        self.len_sub_bytes = None
        self.num_sub_packets = None
        self.idx = idx
        self.version = int(PACKET_STRING[self.idx : self.idx + 3], 2)
        self.version_total = self.version
        self.type = int(PACKET_STRING[self.idx + 3 : self.idx + 6], 2)
        debug(f"{self.version=}  {self.type=}")
        self.idx += 6

        if self.type == 4:
            self.literal = True
            literal_bits = []
            while True:
                literal_bits.append(PACKET_STRING[self.idx + 1 : self.idx + 5])
                ret = PACKET_STRING[self.idx] == "0"
                self.idx += 5
                if ret:
                    self.value = int("".join(literal_bits), 2)
                    debug(f"{self.literal=}  {self.value=}")
                    break
        else:
            # operator
            self.values = []
            if PACKET_STRING[self.idx] == "0":
                self.sub_bytes_type = "len"
                self.len_sub_bytes = int(PACKET_STRING[self.idx + 1 : self.idx + 16], 2)
                self.idx += 16
                target = self.idx + self.len_sub_bytes
                while self.idx < target:
                    self.sub_packet(self.idx)
            else:
                self.sub_bytes_type = "num"
                self.num_sub_packets = int(
                    PACKET_STRING[self.idx + 1 : self.idx + 12], 2
                )
                self.idx += 12
                for n in range(self.num_sub_packets):
                    self.sub_packet(self.idx)

            # Apply operations
            if self.type == 0:
                self.value = sum(self.values)
            elif self.type == 1:
                self.value = math.prod(self.values)
            elif self.type == 2:
                self.value = min(self.values)
            elif self.type == 3:
                self.value = max(self.values)
            elif self.type == 5:
                self.value = 1 if self.values[0] > self.values[1] else 0
            elif self.type == 6:
                self.value = 1 if self.values[0] < self.values[1] else 0
            elif self.type == 7:
                self.value = 1 if self.values[0] == self.values[1] else 0

    def sub_packet(self, idx):
        p = Packet(idx)
        self.idx = p.idx
        self.version_total += p.version_total
        self.values.append(p.value)


def get_bits():
    input_data = common.read_string_file()
    for line in input_data:
        debug(line.strip())
        yield ("".join(HEX_MAPPINGS[c] for c in line.strip()))
        debug("")
    return ""


def process():
    for bits in get_bits():
        global PACKET_STRING
        PACKET_STRING = bits
        p = Packet(0)
        debug(f"{p.value=}")
    return p


def part_1():
    p = process()
    return p.version_total


def part_2():
    p = process()
    debug(f"{p.value=}")
    return p.value
