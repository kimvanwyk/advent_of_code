from collections import Counter
twos = 0
threes = 0
with open('input.txt', 'r') as fh:
    for l in fh:
        d = Counter()
        for c in l.strip():
            d[c] += 1
        if 2 in d.values():
            twos += 1
        if 3 in d.values():
            threes += 1
print(twos*threes)
        
