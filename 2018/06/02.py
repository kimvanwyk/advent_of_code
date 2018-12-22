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

region_size = 0
for x in range(1,max_x+1):
    for y in range(1,max_y+1):
        dists = []
        for point in pd.values():
            dists.append(abs(x-point[0]) + abs(y-point[1]))
        if sum(dists) < 10000:
            region_size += 1

print(region_size)
