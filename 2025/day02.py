import common
from common import debug
import settings

from rich import print


def process():
    with open(settings.settings.input_file, "r") as fh:
        for r in fh.read().strip().split(","):
            yield (r.split("-"))


def part_1():
    total = 0
    for start, end in process():
        for id_num in range(int(start), int(end) + 1):
            if len(str(id_num)) % 2 == 0:
                h = len(str(id_num)) // 2
                if str(id_num)[:h] == str(id_num)[h:]:
                    total += id_num
                    debug(f"Match {start}-{end}: {id_num}")
    return total


def part_2():
    return process()
