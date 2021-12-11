import common
from common import debug
import settings

OPEN = "{[(<"
CLOSE = "}])>"

OPEN_TO_CLOSE = {"{": "}", "[": "]", "(": ")", "<": ">"}
CLOSE_TO_OPEN = {v: k for (k, v) in OPEN_TO_CLOSE.items()}
CORRUPT_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
INCOMPLETE_SCORE = {"(": 1, "[": 2, "{": 3, "<": 4}


def process():
    input_data = common.read_string_file()
    mismatches = []
    unused = []
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
            unused.append(opens)
    return (mismatches, unused)


def part_1():
    (mismatches, unused) = process()
    return sum(CORRUPT_POINTS[m] for m in mismatches)


def part_2():
    (mismatches, unused) = process()
    scores = []
    for u in unused:
        scores.append(0)
        u.reverse()
        debug(u)
        for c in u:
            scores[-1] *= 5
            scores[-1] += INCOMPLETE_SCORE[c]
        debug(scores)
    scores.sort()
    return scores[len(scores) // 2]
