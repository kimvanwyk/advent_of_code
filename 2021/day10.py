import common
from common import debug
import settings

OPEN = "{[(<"
CLOSE = "}])>"

OPEN_TO_CLOSE = {"{": "}", "[": "]", "(": ")", "<": ">"}
CLOSE_TO_OPEN = {v: k for (k, v) in OPEN_TO_CLOSE.items()}
POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def process():
    input_data = common.read_string_file()
    mismatches = []
    for line in input_data:
        opens = []
        for c in line:
            if c in OPEN:
                opens.append(c)
            if c in CLOSE:
                o = opens[-1] if opens else None
                if OPEN_TO_CLOSE.get(o, None) != c:
                    mismatches.append(c)
                    debug(f"{line}- Mismatch on line")
                    break
                opens.pop()
        else:
            debug(f"{line} - No mismatch on line")
    debug(mismatches)
    return sum(POINTS[m] for m in mismatches)


def part_1():
    return process()


def part_2():
    return process()
