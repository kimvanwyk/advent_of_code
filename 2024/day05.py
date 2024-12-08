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


def check_ordering(page, ordering):
    seen = []
    for c in page:
        if any(p in seen for p in ordering[c]):
            return False
            break
        seen.append(c)
    else:
        return True


def part_1():
    (ordering, pages) = process()
    debug(ordering)
    total = 0
    for page in pages:
        if check_ordering(page, ordering):
            debug(f"success: {page}")
            total += page[len(page) // 2]
    return total


def part_2():
    (ordering, pages) = process()
    debug(ordering)
    total = 0
    for page in pages:
        if check_ordering(page, ordering):
            continue
        debug(page)
        i = 0
        while True:
            swapped = False
            if page[i] in ordering:
                for j in range(i):
                    if page[j] in ordering[page[i]]:
                        (page[j], page[i]) = (page[i], page[j])
                        swapped = True
                        i = 0
                        break
            if swapped is False:
                i += 1
            if i == len(page):
                debug(page)
                total += page[len(page) // 2]
                break
    return total
