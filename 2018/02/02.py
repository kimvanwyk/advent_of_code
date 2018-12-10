from collections import Counter
import sys
twos = 0
threes = 0
ids = []
with open('input.txt', 'r') as fh:
    for l in fh:
        d = Counter()
        i = l.strip()
        for c in i:
            d[c] += 1
        if any(x in d.values() for x in (2,3)):
            ids.append(i)
for i in ids:
    for j in ids:
        diffs = 0
        out = []
        if i != j:
            for (a,b) in zip(i,j):
                if a != b:
                    diffs += 1
                else:
                    out.append(a)
        if diffs == 1:
            print(i)
            print(j)
            print(''.join(out))
            sys.exit(1)
        
