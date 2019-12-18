from collections import defaultdict
FIN = "1.txt"

asteroids = []
with open(FIN) as fh:
    for l in fh:
        asteroids.append([])
        for i in l.strip():
            asteroids[-1].append(i)

for a in asteroids:
    print(' '.join(a))

mx = len(asteroids[-1]) - 1
my = len(asteroids) - 1
edges = []

for x in range(mx + 1):
    if ((x,0)) not in edges:
        edges.append((x,0))
for y in range(my + 1):
    if ((0,y)) not in edges:
        edges.append((0,y))
for x in range(mx + 1):
    if ((x,my)) not in edges:
        edges.append((x,my))
for y in range(my + 1):
    if ((mx,y)) not in edges:
        edges.append((mx,y))
# edges = list(set(edges))
# edges.sort()
# print('edges:', edges)

def get_num_hits(x,y,debug=False):
    num_hits = 0
    hits = []
    for (ex,ey) in edges:
        if ex == x:
            m = 1
            dx = 0
        else:
            if ex < x:
                dx = -1
            else:
                dx = 1

            if ey == y:
                m = 0
            else:
                m = abs(y - ey) / abs(x - ex)

        if ey <= y and m:
            m = -m

        if debug:
            print('ex:', ex, 'x:', x, 'ey:', ey, 'y:', y, 'dx:', dx, 'm:', m)

        points = []
        (sx,sy) = (x,y)
        while True:
            sx += dx
            sy += m
            if not ((sx >= 0) and (sx <= mx) and (sy >= 0) and (sy <= my)):
                break
            diff = abs(int(sy) - sy)
            iy = int(round(sy))
            if diff > 0.9:
                diff = 1 - diff
            print('sx:', sx, 'sy:', sy, diff)
            if (diff < 0.0001):
                print('hits:', hits, 'sx:', sx, 'sy:', sy)
                if (asteroids[iy][sx] == '#') and ((sx,iy) not in hits):
                    print('hit, x', sx, 'y', iy)
                    points.append((sx, iy))
                    num_hits += 1
                    hits.append((sx,iy))
                    break
                if (sx,iy) == (ex,ey):
                    break
        if debug:
            print('points:', points)
            res = []
            for a in asteroids:
                res.append(a[:])
            for (px, py) in points:
                if res[py][px] == '#':
                    p = 'h'
                else:
                    p = 'X'
                res[py][px] = p
            if res[ey][ex] in ('#', 'h'):
                p = 'H'
            else:
                p = 'E'
            res[ey][ex] = p
            res[y][x] = 'S'
            if debug:
                for a in res:
                    print(' '.join(a))
        if debug:
            print(num_hits)
    return(num_hits)

hits = defaultdict(list)
for x in range(mx+1):
    for y in range(my+1):
        if asteroids[y][x] == '#':
            hits[get_num_hits(x,y)].append((x,y))
# hits[get_num_hits(0,2,True)].append((0,2))
keys = list(hits.keys())
keys.sort(reverse=True)
for k in keys:
    print(k, hits[k])
if 1:
    for a in asteroids:
        print(' '.join(a))
