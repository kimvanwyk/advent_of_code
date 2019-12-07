inputs = ['B)C','C)D','D)E','COM)B','E)F','B)G','G)H','D)I','E)J','J)K','K)L']

in_to_out = {}
out_to_in = {}

for i in inputs:
    (inner, outer) = i.split(')')
    in_to_out.setdefault(inner, []).append(outer)
    out_to_in[outer] = inner
leaves = set(out_to_in.keys()).difference(set(in_to_out.keys()))

print(in_to_out)
print(out_to_in)
print(leaves)

mapping = []
for leaf in leaves:
    node = leaf
    mapping.append([leaf])
    while node != "COM":
        node = out_to_in[node]
        mapping[-1].append(node)
    mapping[-1].reverse()
for m in mapping:
    print(m)

paths = {}
for m in mapping:
    found = []
    for o in m:
        found.append(o)
        paths.setdefault(tuple(found), None)

print(paths)

print(sum(len(m) - 1 for m in paths.keys()))


# current = 'COM'
# prev = []
# mappings = []
# while True:
#     prev.append(current)
#     for node in orbits[current]:
#         current = node
#         if node not in orbits.keys():
#             mappings.append(prev)
#             current 

# checksum = len(orbits['COM'])
# for outer in orbits['COM']:
#     while True:
#         checksum += len(orbits[outer])
