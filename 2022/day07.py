import common
from common import debug
import settings

from attr import define, field

from typing import Optional


@define
class File:
    name: str
    size: int


@define(slots=False)
class Dir:
    path: str
    files: list = field(init=False)
    dirs: list = field(init=False)

    def __attrs_post_init__(self):
        self.files = []
        self.dirs = []

    def size(self, objects):
        return sum([objects[name].size(objects) for name in self.dirs]) + sum(
            f.size for f in self.files
        )


def process():
    current_path = []
    objects = {}
    in_ls = False
    for line in common.read_string_file():
        if line[0] == "$":
            in_ls = False
            if "cd" in line:
                if "/" in line:
                    current_path = []
                elif ".." in line:
                    current_path.pop()
                else:
                    current_path.append(line.split("$ cd ")[-1])
                current_path_str = "/".join(current_path)
            if "ls" in line:
                in_ls = True
        else:
            if in_ls:
                if current_path_str not in objects:
                    objects[current_path_str] = Dir(current_path_str)
                (t, name) = line.split(" ")
                if t == "dir":
                    objects[current_path_str].dirs.append(
                        "/".join(current_path + [name])
                    )
                else:
                    objects[current_path_str].files.append(File(name, int(t)))
    return objects


def part_1():
    objects = process()
    debug(objects)
    total = 0
    for name in objects:
        size = objects[name].size(objects)
        if size <= 100000:
            total += size
    return total


def part_2():
    objects = process()
    required = 30000000 - (70000000 - objects[""].size(objects))
    debug(f"{required=}")
    smallest = 30000000
    for d in objects.values():
        size = d.size(objects)
        # debug(f"{d=} {size=} {size > required=}")
        if size > required:
            debug(f"{d=} {size=} {smallest=} {size<smallest=}")
            if size < smallest:
                smallest = size
    return smallest
