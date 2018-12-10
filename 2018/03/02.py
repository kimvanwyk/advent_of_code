from collections import Counter
from pampy import match, _
import re

p = Counter()
with open('input.txt', 'r') as fh:
    d = {}
    for l in fh:
        # #1 @ 1,3: 4x4
        (ID, left, top, width, height) = match(l.strip(), re.compile('#(\w+) @ (\w+),(\w+): (\w+)x(\w+)'), lambda *args: [int(c) for c in args])
        points = set()
        for h in range(height):
            for w in range(width):
                point = (left+w, top+h)
                points.add(point)
                p[point] += 1
        d[ID] = points


broke = 0
for (ki,i) in d.items():
    for (kj,j) in d.items():
        if ki != kj:
            if i.intersection(j):
                broke += 1
                # print('broke', ki, kj)
                break
    else:
        print(ki)
print(broke)
