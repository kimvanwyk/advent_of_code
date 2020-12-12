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


def check_passport_part2(passport):
    try:
        for (k, low, high) in (
            ("byr", 1920, 2002),
            ("iyr", 2010, 2020),
            ("eyr", 2020, 2030),
        ):
            if not low <= int(passport[k]) <= high:
                return False

        return True
    except Exception as e:
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
