import attr


@attr.s
class Settings:
    test = attr.ib(default=True)
    debug = attr.ib(default=False)
    input_file = attr.ib(default=None)


settings = Settings()
