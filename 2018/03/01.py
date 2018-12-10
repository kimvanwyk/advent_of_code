from collections import Counter
from pampy import match, _
import re

claims = {}
p = Counter()
with open('input.txt', 'r') as fh:
    n = 0
    d = {}
    for l in fh:
        # #1 @ 1,3: 4x4
        (ID, left, top, width, height) = match(l.strip(), re.compile('#(\w+) @ (\w+),(\w+): (\w+)x(\w+)'), lambda *args: [int(c) for c in args])
        points = {(left, top),}
        for h in range(height):
            for w in range(width):
                point = (left+w, top+h)
                points.add(point)
                p[point] += 1
        d[ID] = points

print(len([c for c in p.values() if c > 1]))

