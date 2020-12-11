def read_integer_file(fn):
    with open(fn, "r") as fh:
        return [int(line.strip()) for line in fh.readlines()]
