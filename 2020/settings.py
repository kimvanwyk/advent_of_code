import attr


@attr.s
class Settings:
    test = attr.ib(default=True)
    debug = attr.ib(default=False)
    input_file = attr.ib(default=None)
    day = attr.ib(default=None)

    def set_day(self, day):
        self.day = int(day)
        self.input_file = f"day{self.day:02}_{'test_' if self.test else ''}input.txt"


settings = Settings()
