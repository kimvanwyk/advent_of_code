import common
from common import debug
import settings

from rich import print

import functools
import operator
import os
import re
import sqlite3


class Processor:
    def __init__(self):
        try:
            os.remove("day06.db")
        except Exception:
            pass
        self.con = sqlite3.connect("day06.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE vals (col, value)")
        self.cur.execute("CREATE TABLE operators (col, operator)")

        for l in common.read_string_file():
            for n, m in enumerate(re.finditer("\\S+", l), 0):
                if l[0] in ("+", "*"):
                    self.cur.execute(
                        f"INSERT INTO operators VALUES ({n},'{m.group(0)}');"
                    )
                else:
                    self.cur.execute(f"INSERT INTO vals VALUES ({n},'{m.group(0)}');")
        self.num_cols = n + 1


def part_1():
    processor = Processor()
    total = 0
    print(processor.num_cols)
    for n in range(processor.num_cols):
        op = (
            operator.add
            if processor.cur.execute(
                f"SELECT operator FROM operators WHERE col = {n}"
            ).fetchone()[0]
            == "+"
            else operator.mul
        )
        debug(n, op)
        result = functools.reduce(
            op,
            (
                int(v[0])
                for v in processor.cur.execute(
                    f"SELECT value FROM vals WHERE col = {n}"
                ).fetchall()
            ),
        )
        debug(result)
        total += result
    return total


def part_2():
    return process()
