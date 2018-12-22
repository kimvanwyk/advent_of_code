import string

with open('input.txt', 'r') as fh:
    points = [i.strip().split(',') for i in [l.strip() for l in fh]]
    
num_first = int((len(points) / len(string.ascii_uppercase))) + 1
first = ''.join((f * len(string.ascii_uppercase) for f in string.ascii_uppercase[:num_first]))
pd = {}
for (k, point) in zip((zip(first, string.ascii_uppercase * num_first)), points):
    pd[''.join(k)] = (int(point[0].strip()), int(point[1].strip()))

max_x = 0
max_y = 0
for (x,y) in pd.values(): 
    max_x = x if max_x < x else max_x
    max_y = y if max_y < y else max_y

# max_x = 25
# max_y = 5

regions = {}
for x in range(1,max_x+1):
    for y in range(1,max_y+1):
        dists = []
        for (k,point) in pd.items():
            dists.append((abs(x-point[0]) + abs(y-point[1]), k))
        dists.sort()
        if dists[0][0] < dists[1][0]:
            k = dists[0][1]
            if any((x in (1, max_x), y in (1, max_y))):
                regions[k] = None
            val = regions.get(k, 0)
            if val is not None:
                val += 1
            if val:
                regions[k] = val
rl = [(v,k) for (k,v) in regions.items() if v is not None]
rl.sort()
print(rl)
print(rl[-1])

