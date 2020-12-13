import importlib

import pyperclip

import settings

settings.settings.test = False


def run_day_part(day, part):
    settings.settings.set_day_and_part(day, part)
    day_mod = importlib.import_module(f"day{day:02}")
    return getattr(day_mod, f"part_{part}")()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Executor for 2020 Advent of Code challenges")
    parser.add_argument(
        "day", type=int, choices=range(1, 26), help="The day to execute"
    )
    parser.add_argument("part", type=int, choices=(1, 2), help="The part to execute")
    parser.add_argument(
        "data", choices=("t", "p"), help="Whether to run with test (t) or prod (p) data"
    )
    parser.add_argument("-d", action="store_true", help="Whether to include debug")
    parser.add_argument(
        "-p",
        choices=(1, 2),
        default=None,
        type=int,
        help="If test data is in parts, which part to use. Will override part setting",
    )
    args = parser.parse_args()

    settings.settings.test = args.data == "t"
    settings.settings.debug = args.d

    part = args.part
    if args.p:
        part = args.p
    result = run_day_part(args.day, part)
    print(result)
    pyperclip.copy(result)
