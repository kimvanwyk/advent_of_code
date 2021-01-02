import common
from common import debug
import settings


def boolify(char):
    return char == "#"


def process():
    input_data = common.read_string_file()
    tiles = {}
    for line in input_data:
        if "Tile" in line:
            tid = int(line[5:-1])
            tiles[tid] = {"t": [], "l": [], "r": [], "b": []}
            n = -1
        else:
            if line:
                if n < 0:
                    length = len(line)
                n += 1
                if n == 0:
                    tiles[tid]["t"] = [boolify(c) for c in line]
                elif n == length - 1:
                    tiles[tid]["b"] = [boolify(c) for c in line]
                tiles[tid]["l"].append(boolify(line[0]))
                tiles[tid]["r"].append(boolify(line[-1]))
    return tiles


def part_1():
    tiles = process()
    debug(tiles[2311])


def part_2():
    return process()
