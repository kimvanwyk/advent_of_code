import common
from common import debug
import settings


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
        self.idx = idx
        self.version = int(PACKET_STRING[self.idx : self.idx + 3], 2)
        self.type = int(PACKET_STRING[self.idx + 3 : self.idx + 6], 2)
        self.idx += 6

        if self.type == 4:
            self.literal = True
            literal_bits = []
            while True:
                literal_bits.append(PACKET_STRING[self.idx + 1 : self.idx + 5])
                ret = PACKET_STRING[self.idx] == "0"
                self.idx += 5
                if ret:
                    debug("".join(literal_bits))
                    self.value = int("".join(literal_bits), 2)
                    break


def get_bits():
    input_data = common.read_string_file()
    for line in input_data:
        yield ("".join(HEX_MAPPINGS[c] for c in line.strip()))
    return ""


def process():
    for bits in get_bits():
        global PACKET_STRING
        PACKET_STRING = bits
        p = Packet(0)
        debug(f"{p.version=}  {p.type=}")
        if p.literal:
            debug(f"{p.literal=}  {p.value=}")
        debug("")


def part_1():
    process()
    return ""


def part_2():
    return process()
