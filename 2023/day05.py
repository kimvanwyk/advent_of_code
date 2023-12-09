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
                maps[map_name][(src_start, src_start + rng - 1)] = dst_start
    return seeds, maps


def get_dest_from_dict(d: dict, src: int):
    for (src_start, src_end), dst_start in d.items():
        if src_start <= src <= src_end:
            return dst_start + (src - src_start)
    return src


def process_chain(maps: list, seed: int):
    soil = get_dest_from_dict(maps["seed-to-soil"], seed)
    fertilizer = get_dest_from_dict(maps["soil-to-fertilizer"], soil)
    water = get_dest_from_dict(maps["fertilizer-to-water"], fertilizer)
    light = get_dest_from_dict(maps["water-to-light"], water)
    temperature = get_dest_from_dict(maps["light-to-temperature"], light)
    humidity = get_dest_from_dict(maps["temperature-to-humidity"], temperature)
    location = get_dest_from_dict(maps["humidity-to-location"], humidity)
    # debug((soil, fertilizer, water, light, temperature, humidity, location))
    return (soil, fertilizer, water, light, temperature, humidity, location)


def part_1():
    (seeds, maps) = process()
    debug(seeds)
    debug(maps)
    min_loc = 1000000000
    for seed in seeds:
        (
            soil,
            fertilizer,
            water,
            light,
            temperature,
            humidity,
            location,
        ) = process_chain(maps, seed)
        if location < min_loc:
            min_loc = location
        # debug((soil, fertilizer, water, light, temperature, humidity, location))
    return min_loc


def part_2():
    (seed_nums, maps) = process()
    min_loc = 100000000000000
    seen = {}
    for n in range(0, len(seed_nums), 2):
        seed = seed_nums[n]
        while seed < (seed_nums[n] + seed_nums[n + 1]):
            if seed in seen:
                continue
            seen[seed] = 1
            (
                soil,
                fertilizer,
                water,
                light,
                temperature,
                humidity,
                location,
            ) = process_chain(maps, seed)
            if location < min_loc:
                min_loc = location
            # debug((soil, fertilizer, water, light, temperature, humidity, location))
            seed += 1
            print(seed)
    return min_loc
