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


# Sought help from https://www.reddit.com/r/adventofcode/comments/kc4njx/2020_day_13_solutions/gfok4yk/
# Learned about Chinese Remainder Theorem
# Also hadn't noticed the bus values of interest were all primes
def find_time_pattern():
    results = []
    (timestamp, bus_times) = process()
    for (num, bus_time) in enumerate(bus_times, 0):
        diffs = {bus: -idx % bus for (idx, bus) in enumerate(bus_time) if bus}
        divisors = list(reversed(sorted(diffs)))
        timestamp = diffs[divisors[0]]
        product = divisors[0]
        for divisor in divisors[1:]:
            while (timestamp % divisor) != diffs[divisor]:
                timestamp += product
            product *= divisor
        results.append(timestamp)
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
    results = find_time_pattern()
    debug(results)
    return results[0]
