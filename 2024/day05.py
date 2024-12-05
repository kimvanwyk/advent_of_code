import common
from common import debug
import settings

from collections import defaultdict

from rich import print


def process():
    ordering = defaultdict(list)
    pages = []
    for l in common.read_string_file():
        if "|" in l:
            (k, v) = l.split("|")
            ordering[int(k)].append(int(v))
        elif "," in l:
            pages.append([int(c) for c in l.split(",")])
    return (ordering, pages)


def part_1():
    (ordering, pages) = process()
    debug(ordering)
    total = 0
    for page in pages:
        seen = []
        for c in page:
            if any(p in seen for p in ordering[c]):
                debug(f"fail: {page}")
                break
            seen.append(c)
        else:
            debug(f"success: {page}")
            total += page[len(page) // 2]
    return total


def part_2():
    return process()
