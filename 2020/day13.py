import common
from common import debug
import settings


def process():
    input_data = [l for l in common.read_string_file()]
    timestamp = int(input_data[0])
    bus_times = []
    for bus_time in [bt for bt in input_data[1:]]:
        bus_times.append(
            [int(bus) if bus != "x" else None for bus in bus_time.split(",")]
        )
    debug(bus_times)
    return (timestamp, bus_times)


def part_1():
    (timestamp, bus_times) = process()
    floor = timestamp - 1
    delays = [(((floor // bus) + 1) * bus, bus) for bus in bus_times[0] if bus]
    delays.sort()
    result = (delays[0][0] - timestamp) * delays[0][1]
    debug(delays)
    debug(delays[0], result)
    return result


def part_2():
    return process()
