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


def find_time_pattern(starting_value=0):
    results = []
    (timestamp, bus_times) = process()
    for (num, bus_time) in enumerate(bus_times, 0):
        timestamp = (starting_value // bus_time[0]) * bus_time[0]
        cont = True
        print(num, bus_time, starting_value, timestamp)
        while cont:
            for (idx, bus) in enumerate(bus_time[1:], 1):
                if bus:
                    if (timestamp + idx) % bus:
                        timestamp += bus_time[0]
                        break
            else:
                cont = False
            if cont:
                continue
            results.append(timestamp)
            debug((num, timestamp))
            cont = False
    return results


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
    if not settings.settings.test:
        starting_value = 100000000000000 - 1
    else:
        starting_value = 2000
    results = find_time_pattern(starting_value)
    return results[0]
