import common
from common import debug
import settings

from rich import print


def process_p1():
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


def process_p2():
    maps = {}
    for l in common.read_string_file():
        if l:
            if "seeds" in l:
                seeds = [int(c) for c in l.split(": ")[-1].strip().split(" ")]
            elif "map:" in l:
                map_name = l.split(" ")[0].split("-")[-1]
                maps[map_name] = {}
            else:
                (dst_start, src_start, rng) = [int(c) for c in l.split(" ")]
                maps[map_name][(dst_start, rng)] = src_start - dst_start
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


def get_dest_from_dict_p2(d: dict, src: int):
    for (src_start, length), diff in d.items():
        if src_start <= src <= src_start + length:
            return src + diff
    return src


def process_chain_reverse(maps: list, location: int):
    humidity = get_dest_from_dict_p2(maps["location"], location)
    temperature = get_dest_from_dict_p2(maps["humidity"], humidity)
    light = get_dest_from_dict_p2(maps["temperature"], temperature)
    water = get_dest_from_dict_p2(maps["light"], light)
    fertilizer = get_dest_from_dict_p2(maps["water"], water)
    soil = get_dest_from_dict_p2(maps["fertilizer"], fertilizer)
    seed = get_dest_from_dict_p2(maps["soil"], soil)
    # debug((humidity, temperature, light, water, fertilizer, soil, seed))
    return (humidity, temperature, light, water, fertilizer, soil, seed)


def part_1():
    (seeds, maps) = process_p1()
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


def check_location(maps, seed_ranges, location):
    (
        humidity,
        temperature,
        light,
        water,
        fertilizer,
        soil,
        seed,
    ) = process_chain_reverse(maps, location)
    # debug(
    #     (
    #         location,
    #         (
    #             humidity,
    #             temperature,
    #             light,
    #             water,
    #             fertilizer,
    #             soil,
    #             seed,
    #         ),
    #     )
    # )
    for seed_start, seed_end in seed_ranges:
        debug(
            (
                location,
                seed,
                seed_start,
                seed_end,
                seed_start <= seed <= seed_end,
            )
        )
        if seed_start <= seed <= seed_end:
            return True
    return False


def part_2():
    (seed_nums, maps) = process_p2()
    seed_ranges = []
    for n in range(0, len(seed_nums), 2):
        seed_ranges.append((seed_nums[n], seed_nums[n] + seed_nums[n + 1]))
    debug(seed_ranges)
    debug(maps)
    debug("")
    location = 0
    while True:
        if check_location(maps, seed_ranges, location):
            return location
        location += 1
