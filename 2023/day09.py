import common
from common import debug
import settings

from rich import print


def process(location="end"):
    results = []
    for l in common.read_string_file():
        history = [int(c.strip()) for c in l.split()]
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
            if location == "end":
                rows[n].append(rows[n][-1] + rows[n + 1][-1])
            else:
                rows[n].insert(0, rows[n][0] - rows[n + 1][0])
        for row in rows:
            debug(row)
        results.append(rows[0][-1 if location == "end" else 0])
    debug(results)
    return sum(results)


def part_1():
    return process()


def part_2():
    return process(location="start")
