# Create template files for a new day

import os, os.path
import shutil
from subprocess import call
import sys


def new_day(day):
    fn = f"day{day:02}"
    py_fn = f"{fn}.py"
    test_input_fn = f"{fn}_test_input.txt"
    input_fn = f"{fn}_input.txt"

    if not os.path.exists(py_fn):
        shutil.copy2("template.py", py_fn)

    for f in (test_input_fn, input_fn):
        if not os.path.exists(f):
            with open(f, "w") as fh:
                fh.write("Replace Me\n")

    call(f"git add {py_fn} {test_input_fn} {input_fn}", shell=True)


new_day(int(sys.argv[1]))
