import pprint

import attr

import common
import settings


def parse_lines():
    passports = []

    def add_passport_dict(items):
        passports.append(dict([item.split(":") for item in items]))

    items = []
    for line in common.read_string_file():
        if line:
            items.extend([l.strip() for l in line.split(" ")])
        else:
            add_passport_dict(items)
            items = []
    if items:
        add_passport_dict(items)
    return passports


def check_passport_part1(passport):
    return all(
        [c in passport for c in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")]
    )


def check_passport_part2(passport, height_ranges={"cm": (150, 193), "in": (59, 76)}):
    try:
        # year range tests
        for (k, low, high) in (
            ("byr", 1920, 2002),
            ("iyr", 2010, 2020),
            ("eyr", 2020, 2030),
        ):
            if not low <= int(passport[k]) <= high:
                return False

        hgt = passport["hgt"]
        unit = hgt[-2:]
        if unit not in height_ranges:
            return False
        if not height_ranges[unit][0] <= int(hgt[:-2]) <= height_ranges[unit][1]:
            return False

        hcl = passport["hcl"]
        if not all(
            [
                hcl[0] == "#",
                len(hcl) == 7,
                all([c in "0123456789abcdef" for c in hcl[1:]]),
            ]
        ):
            return False

        if passport["ecl"] not in "amb blu brn gry grn hzl oth".split(" "):
            return False

        return True
    except Exception as e:
        if settings.settings.debug:
            print(e)
        return False


def process(check):
    passports = parse_lines()
    valids = 0
    for passport in passports:
        result = check(passport)
        if result:
            valids += 1
        if settings.settings.debug:
            pprint.pprint(passport)
            print(result)
    return valids


def part_1():
    return process(check_passport_part1)


def part_2():
    return process(check_passport_part2)
