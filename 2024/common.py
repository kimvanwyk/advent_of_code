from attrs import define
from rich import print

import settings


def read_integer_file(fn=None):
    return (int(line) for line in read_string_file(fn))


def read_string_file(fn=None):
    if fn is None:
        fn = settings.settings.input_file
    with open(fn, "r") as fh:
        for line in fh:
            yield line.strip()


def debug(*m):
    if settings.settings.debug:
        print(*m)


def idempotent(object):
    return object


@define
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __hash__(self):
        return hash((self.x, self.y))
