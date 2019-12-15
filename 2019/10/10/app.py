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

mx = len(asteroids[-1])
my = len(asteroids)
edges = []
for x in range(mx):
    edges.append((x,0))
for y in range(my):
    edges.append((0,y))
for x in range(mx):
    edges.append((x,my - 1))
for y in range(my):
    edges.append((mx - 1,y))
# edges = [(3,0),(2,0),(1,0),(0,0),(0,1)]
# edges = [(2,0),(1,0),(0,0),(0,1)]
print('edges:', edges)
print()

(x,y) = (3,4)
num_hits = 0
for (ex,ey) in edges:
    if ex == x:
        m = 1
        dx = 0
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
    if x > ex:
        op = operator.sub
    else:
        op = operator.add
    if m is not None:
        while True:
            sx = op(sx, dx)
            sy = sy + m
            if not ((sx >= 0) and (sx < mx) and (sy >= 0) and (sy < my)):
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
            if res[ey][ex] == '#':
                p = 'H'
            else:
                p = 'E'
            res[ey][ex] = p
            res[y][x] = 'S'
            for a in res:
                print(' '.join(a))

        print()
print(num_hits)
