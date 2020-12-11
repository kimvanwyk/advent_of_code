from collections import defaultdict
FIN = "2.txt"

asteroids = []
with open(FIN) as fh:
    for l in fh:
        asteroids.append([])
        for i in l.strip():
            asteroids[-1].append(i)

colours = {'#': 'black', '.': 'yellow', 'S': 'red'}
n = 0
with open('out.html', 'w') as fh:
    fh.write("<html><body>\n<table border='1'><tr>\n")
    for (y,row) in enumerate(asteroids):
        fh.write('<tr>')
        for (x,cell) in enumerate(row):
            if (x,y) == (5,8):
                cell = 'S'
            fh.write((f"<td width='20px' height='20px' bgcolor='{colours[cell]}'></td>"))
        fh.write('</tr>')
    fh.write('</table></body></html>')

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

d = [(0,-1.0)]
for dx in (-1,1):
    m = -0.999
    while m < 1.0:
        d.append((dx,m))
        m += 0.001
d.append((0,1.0))

def get_num_hits(x,y,debug=False):
    num_hits = 0
    hits = []
    # for (ex,ey) in edges:
    for (dx,dy) in d:
        if debug:
            print('x:', x, 'y:', y, 'dx:', dx, 'dy:', dy)
        points = []
        (sx,sy) = (x,y)
        while True:
            sx += dx
            sy += dy
            diff = abs(int(sy) - sy)
            iy = int(round(sy))
            if diff > 0.95:
                diff = 1 - diff
            if debug:
                print('sx:', sx, 'sy:', sy, 'diff:', diff, 'iy:', iy)
            # if not ((sx > 0) and (sx <= mx) and (iy >= 0) and (iy <= my)):
            if ((sx < 0) or (sx > mx) or (iy < 0) or (iy > my)):
                break
            if (diff < 0.0001):
                if debug:
                    print('hits:', hits, 'sx:', sx, 'sy:', sy)
                if (asteroids[iy][sx] == '#') and ((sx,iy) not in hits):
                    if debug:
                        print('hit, x', sx, 'y', iy)
                    points.append((sx, iy))
                    num_hits += 1
                    hits.append((sx,iy))
                    break
        # if debug:
        #     print('points:', points)
        #     res = []
        #     for a in asteroids:
        #         res.append(a[:])
        #     for (px, py) in points:
        #         if res[py][px] == '#':
        #             p = 'h'
        #         else:
        #             p = 'X'
        #         res[py][px] = p
        #     if res[ey][ex] in ('#', 'h'):
        #         p = 'H'
        #     else:
        #         p = 'E'
        #     res[ey][ex] = p
        #     res[y][x] = 'S'
        #     if debug:
        #         for a in res:
        #             print(' '.join(a))
        if debug:
            print(num_hits)
    return(num_hits)

hits = defaultdict(list)
# for x in range(mx+1):
#     for y in range(my+1):
#         if asteroids[y][x] == '#':
#             hits[get_num_hits(x,y)].append((x,y))
hits[get_num_hits(5,8,True)].append((5,8))
# print(d)
keys = list(hits.keys())
keys.sort(reverse=True)
for k in keys:
    print(k, hits[k])
if 1:
    for a in asteroids:
        print(' '.join(a))
