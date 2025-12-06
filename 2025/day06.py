import common
from common import debug
import settings

from rich import print

from collections import defaultdict
import functools
import operator
import os
import re
import sqlite3


class Processor:
    def process_part_1(self):
        try:
            os.remove("day06.db")
        except Exception:
            pass
        self.con = sqlite3.connect("day06.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE vals (col, value)")
        self.cur.execute("CREATE TABLE operators (col, operator)")

        self.cols = defaultdict(list)
        self.operators = {}
        for l in common.read_string_file():
            for n, m in enumerate(re.finditer("\\S+", l), 0):
                if l[0] in ("+", "*"):
                    self.cur.execute(
                        f"INSERT INTO operators VALUES ({n},'{m.group(0)}');"
                    )
                else:
                    self.cur.execute(f"INSERT INTO vals VALUES ({n},'{m.group(0)}');")
        self.num_cols = n + 1

    def process_part_2(self):
        for l in common.read_string_file():
            for i, c in enumerate(l, 0):
                if c in ("+", "*"):
                    self.operators[n] = operator.add if c == "+" else operator.mul
                else:
                    self.cols[i].append(c)
            debug(self.operators)
            debug(self.cols)

    def get_operator(self, col_num: int):
        return (
            operator.add
            if self.cur.execute(
                f"SELECT operator FROM operators WHERE col = {col_num}"
            ).fetchone()[0]
            == "+"
            else operator.mul
        )


def part_1():
    processor = Processor()
    processor.process_part_1()
    total = 0
    for n in range(processor.num_cols):
        op = processor.get_operator(n)
        result = functools.reduce(
            op,
            (
                int(v[0])
                for v in processor.cur.execute(
                    f"SELECT value FROM vals WHERE col = {n}"
                ).fetchall()
            ),
        )
        total += result
    return total


def part_2():
    processor = Processor()
    total = 0
    print(processor.num_cols)
    for n in range(processor.num_cols):
        op = processor.get_operator(n)
        debug(n, op)
        max_len = processor.cur.execute(
            f"SELECT MAX(LENGTH(value)) FROM vals WHERE col = {n}"
        ).fetchone()[0]
        debug(max_len)
        # result = functools.reduce(
        #     op,
        #     (
        #         int(v[0])
        #         for v in processor.cur.execute(
        #             f"SELECT value FROM vals WHERE col = {n}"
        #         ).fetchall()
        #     ),
        # )
        # debug(result)
        # total += result
    return total
