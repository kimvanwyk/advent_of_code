import common
from common import debug
import settings

from rich import print


def process():
    d = {}
    row = 1
    for l in common.read_string_file():
        if not l:
            yield d
            d = {}
            row = 1
        else:
            debug(l)
            for col, c in enumerate(l, 1):
                d[(col, row)] = c
            row += 1
    yield d


def part_1():
    results = []
    for d in process():
        # debug(d)
        max_col = max([k[0] for k in d if k[1] == 1])
        max_row = max([k[1] for k in d if k[0] == 1])
        for line, max_direction, max_edge in (
            ("col", max_col, max_row),
            ("row", max_row, max_col),
        ):
            for direction in range(1, max_direction):
                found = True
                for edge in range(1, max_edge + 1):
                    c = 0
                    while True:
                        if (direction - c) < 1 or (direction + c + 1) > max_direction:
                            break
                        if line == "col":
                            left = d[(direction - c, edge)]
                            right = d[(direction + 1 + c, edge)]
                        else:
                            left = d[(edge, direction - c)]
                            right = d[(edge, direction + 1 + c)]
                        debug(
                            (
                                direction,
                                edge,
                                c,
                                (direction - c),
                                (direction + c + 1),
                                left,
                                right,
                            )
                        )
                        if left != right:
                            found = False
                            break
                        c += 1
                    if found is False:
                        break

                if found is True:
                    results.append((line, direction))
                    break
            if found is True:
                break

        debug(results)
        result = 0
        for direction, index in results:
            result += index * (1 if direction == "col" else 100)
    return result


def part_2():
    return process()
