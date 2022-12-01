import os

import attr


@attr.s
class Settings:
    test = attr.ib(default=True)
    debug = attr.ib(default=False)
    input_file = attr.ib(default=None)
    day = attr.ib(default=None)
    part = attr.ib(default=None)

    def set_day_and_part(self, day, part, test_part=None):
        if test_part is None:
            test_part = part
        self.day = int(day)
        self.part = int(part)

        # Try with part, exclude part from fn if no match found
        fn = f"day{self.day:02}_{'test_' if self.test else ''}input_part{test_part}.txt"
        if fn not in os.listdir():
            fn = f"day{self.day:02}_{'test_' if self.test else ''}input.txt"
        self.input_file = fn


settings = Settings()
