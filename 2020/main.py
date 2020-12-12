import importlib

import settings

settings.settings.test = False


def run_day_part(day, part):
    settings.settings.set_day(day)
    day_mod = importlib.import_module(f"day{day:02}")
    getattr(day_mod, f"part_{part}")()


run_day_part(1, 1)
run_day_part(1, 2)
