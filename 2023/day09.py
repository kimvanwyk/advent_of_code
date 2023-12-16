import common
from common import debug
import settings

from rich import print


def process():
    for l in common.read_string_file():
        yield [int(c.strip()) for c in l.split()]


def part_1():
    results = []
    for history in process():
        debug(f"{history=}")
        rows = [history[:]]
        while True:
            diffs = rows[-1]
            rows.append([])
            for n in range(1, len(diffs)):
                rows[-1].append(diffs[n] - diffs[n - 1])
            if all([c == 0 for c in rows[-1]]):
                rows[-1].append(0)
                break
        for n in range(len(rows) - 2, -1, -1):
            rows[n].append(rows[n][-1] + rows[n + 1][-1])
        for row in rows:
            debug(row)
        results.append(rows[0][-1])
    debug(results)
    return sum(results)


def part_2():
    return process()
