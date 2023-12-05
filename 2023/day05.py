import common
from common import debug
import settings

from rich import print


def process():
    maps = {}
    for l in common.read_string_file():
        if l:
            if "seeds" in l:
                seeds = [int(c) for c in l.split(": ")[-1].strip().split(" ")]
            elif "map:" in l:
                map_name = l.split(" ")[0]
                maps[map_name] = {}
            else:
                (dst_start, src_start, rng) = [int(c) for c in l.split(" ")]
                for src, dst in zip(
                    range(src_start, src_start + rng), range(dst_start, dst_start + rng)
                ):
                    maps[map_name][src] = dst
    return seeds, maps


def part_1():
    (seeds, maps) = process()
    debug(seeds)
    # debug(maps)
    min_loc = 1000000000
    for seed in seeds:
        soil = maps["seed-to-soil"].get(seed, seed)
        fertilizer = maps["soil-to-fertilizer"].get(soil, soil)
        water = maps["fertilizer-to-water"].get(fertilizer, fertilizer)
        light = maps["water-to-light"].get(water, water)
        temperature = maps["light-to-temperature"].get(light, light)
        humidity = maps["temperature-to-humidity"].get(temperature, temperature)
        location = maps["humidity-to-location"].get(humidity, humidity)
        if location < min_loc:
            min_loc = location
        debug((soil, fertilizer, water, light, temperature, humidity, location))
    return min_loc


def part_2():
    return process()
