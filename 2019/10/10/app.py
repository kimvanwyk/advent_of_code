import operator

FIN = "1.txt"

asteroids = []
with open(FIN) as fh:
    for l in fh:
        asteroids.append([])
        for i in l.strip():
            asteroids[-1].append(i)

for a in asteroids:
    print(' '.join(a))

# print(len(asteroids), len(asteroids[-1]))

mx = len(asteroids[-1]) - 1
my = len(asteroids) - 1
edges = []
for x in range(mx + 1):
    edges.append((x,0))
for y in range(my + 1):
    edges.append((0,y))
for x in range(mx + 1):
    edges.append((x,my))
for y in range(my + 1):
    edges.append((mx,y))
edges = list(set(edges))
edges.sort()
# edges = [(3,0),(2,0),(1,0),(0,0),(0,1)]
# edges = [(2,0),(1,0),(0,0),(0,1)]

(x,y) = (3,4)
num_hits = 0
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
    print('ex:', ex, 'x:', x, 'ey:', ey, 'y:', y, 'm:', m)

    points = []
    (sx,sy) = (x,y)
    while True:
        sx += dx
        sy += m
        if not ((sx >= 0) and (sx <= mx) and (sy >= 0) and (sy <= my)):
            break
        # print('op:', op, 'sx:', sx, 'sy:', sy, 'int:', (not sx % 1) and (not sy % 1))
        if (not sx % 1) and (not sy % 1):
            points.append((int(sx), int(sy)))
    print('points:', points)
    if points:
        for (px, py) in points:
            if asteroids[py][px] == '#':
                num_hits += 1
                print('hit at', (px, py))
                break
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
        if 1:
            for a in res:
                print(' '.join(a))

        print()
for a in asteroids:
    print(' '.join(a))
print(num_hits)
print('edges:', edges)
print()
