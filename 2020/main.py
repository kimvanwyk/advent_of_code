import importlib

import settings

settings.settings.test = False


def run_day_part(day, part):
    settings.settings.set_day(day)
    day_mod = importlib.import_module(f"day{day:02}")
    getattr(day_mod, f"part_{part}")()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Executor for 2020 Advent of Code challenges")
    parser.add_argument(
        "day", type=int, choices=range(1, 26), help="The day to execute"
    )
    parser.add_argument("part", type=int, choices=(1, 2), help="The part to execute")
    parser.add_argument(
        "data", choices=("test", "prod"), help="Whether to run with test or prod data"
    )
    parser.add_argument("--debug", action="store_true", help="Whether to include debug")
    args = parser.parse_args()

    settings.settings.test = args.data == "test"
    settings.settings.debug = args.debug

    run_day_part(args.day, args.part)
