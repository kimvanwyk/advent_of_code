import common
from common import debug
import settings

import attr
import os
import sqlite3

FN = "day22.sqlite3"


def make_table():
    # try:
    #     os.remove(FN)
    # except Exception:
    #     pass
    # con = sqlite3.connect(FN)
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE points(x, y, z, PRIMARY KEY (x,y,z))")
    return cur


class BadRange(Exception):
    pass


@attr.define
class Instruction:
    position: bool
    db_cursor: sqlite3.Cursor
    x_range: tuple = ()
    y_range: tuple = ()
    z_range: tuple = ()

    def set_range(self, axis, minval, maxval, limit=None):
        if limit is not None:
            if minval > limit:
                raise BadRange
            if maxval < -limit:
                raise BadRange
            if minval < -limit:
                minval = -limit
            if maxval > limit:
                maxval = limit
            if (maxval - minval) < 0:
                raise BadRange
        setattr(self, f"{axis}_range", range(minval, maxval + 1))

    def apply_points(self):
        for x in self.x_range:
            for y in self.y_range:
                for z in self.z_range:
                    if self.position:
                        try:
                            self.db_cursor.execute(
                                f"INSERT INTO POINTS VALUES ({x}, {y}, {z})"
                            )
                        except sqlite3.IntegrityError:
                            pass
                    else:
                        try:
                            self.db_cursor.execute(
                                f"DELETE FROM POINTS WHERE x = {x} AND y = {y} AND z = {z}"
                            )
                        except Exception:
                            pass


def get_instructions(limit, db_cursor):
    input_data = common.read_string_file()

    for l in input_data:
        (position, range_strings) = l.split(" ")
        ranges = []
        inst = Instruction(position == "on", db_cursor=db_cursor)
        try:
            for range_string in range_strings.split(","):
                inst.set_range(
                    range_string[0],
                    *[int(i) for i in range_string[2:].split("..")],
                    limit=limit,
                )
        except BadRange:
            continue
        yield inst


def process(limit):
    db_cursor = make_table()
    for instruction in get_instructions(limit, db_cursor):
        debug(instruction)
        instruction.apply_points()
    total = db_cursor.execute("SELECT COUNT(*) FROM points").fetchone()[0]
    debug(total)
    return total


def part_1():
    return process(limit=50)


def part_2():
    return process(limit=None)
