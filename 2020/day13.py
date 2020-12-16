import common
from common import debug
import settings


def process():
    input_data = [l for l in common.read_string_file()]
    timestamp = int(input_data[0])
    buses = [int(bus) if bus != "x" else None for bus in input_data[1].split(",")]
    debug(buses)
    return (timestamp, buses)


def part_1():
    (timestamp, buses) = process()
    floor = timestamp - 1
    delays = [(((floor // bus) + 1) * bus, bus) for bus in buses if bus]
    delays.sort()
    result = (delays[0][0] - timestamp) * delays[0][1]
    debug(delays)
    debug(delays[0], result)
    return result


def part_2():
    return process()
