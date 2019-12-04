import copy
import operator

#inputs = [['R8','U5','L5','D3'], ['U7','R6','D4','L4']]
#inputs = [['R75','D30','R83','U83','L12','D49','R71','U7','L72'],['U62','R66','U55','R34','D71','R55','D58','R83']]
#inputs = [['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']]

inputs = []
with open('input.txt', 'r') as fh:
    for l in fh:
        inputs.append(l.strip().split(','))

directions = {'R':(operator.add, 0),
              'L':(operator.sub, 0),
              'U':(operator.add, 1),
              'D':(operator.sub, 1)}

dists = []
points = []
for (n,i) in enumerate(inputs):
    points.append([(100000,100000)])
    dists.append({})
    total = 0
    for move in i:
        (op, index) = directions[move[0]]
        steps = int(move[1:])
        while(steps):
            total += 1
            point = list(copy.copy(points[n][-1]))
            point[index] = op(point[index], 1)
            points[n].append(tuple(point))
            if tuple(point) not in dists[n]:
                dists[n][tuple(point)] = total
            steps -= 1
# print(points[0])
# print(points[1])
intersections = set(points[0]).intersection(points[1])
# print(intersections)
dists = [d for d in [dists[0][point] + dists[1][point] for point in intersections if point in dists[0]] if d]
dists.sort()
print(dists)
