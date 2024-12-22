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


@define(order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def in_bounds(self, min_point, max_point):
        return (min_point.x <= self.x <= max_point.x) and (
            min_point.y <= self.y <= max_point.y
        )


if __name__ == "__main__":
    a = Point(5, 4)
    b = Point(6, 6)
    l = [(a - b), (b - a), (b - a)]
    l.sort()
    print(l)
    print(a.in_bounds(Point(1, 1), Point(10, 10)))
    c = Point(0, -1)
    print(c.in_bounds(Point(1, 1), Point(10, 10)))
