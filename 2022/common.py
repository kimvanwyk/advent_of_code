from rich import print

import settings


def read_integer_file(fn=None):
    return (int(line) for line in read_string_file(fn))


def read_string_file(fn=None):
    if fn is None:
        fn = settings.settings.input_file
    with open(fn, "r") as fh:
        return (line.strip() for line in fh.readlines())


def debug(message):
    if settings.settings.debug:
        print(message)
