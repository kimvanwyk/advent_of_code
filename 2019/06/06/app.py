# inputs = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN", ]
# inputs = ['B)C','C)D','D)E','COM)B','E)F','B)G','G)H','D)I','E)J','J)K','K)L']

inputs = []
with open('input.txt', 'r') as fh:
    for l in fh:
        inputs.append(l.strip())

in_to_out = {}
out_to_in = {}

for i in inputs:
    (inner, outer) = i.split(')')
    in_to_out.setdefault(inner, []).append(outer)
    out_to_in[outer] = inner
leaves = set(out_to_in.keys()).difference(set(in_to_out.keys()))

# print(in_to_out)
# print(out_to_in)
# print(leaves)

mapping = []
for leaf in leaves:
    node = leaf
    mapping.append([leaf])
    while node != "COM":
        node = out_to_in[node]
        mapping[-1].append(node)
for m in mapping:
    if m[0] == 'SAN':
        san = m
    if m[0] == 'YOU':
        you = m
for (n,o) in enumerate(san):
    if o in you:
        print (n,o,you.index(o),n+you.index(o)-2)
        break

# paths = {}
# for m in mapping:
#     found = []
#     for o in m:
#         found.append(o)
#         paths.setdefault(tuple(found), None)

# print(paths)

# print(sum(len(m) - 1 for m in paths.keys()))
