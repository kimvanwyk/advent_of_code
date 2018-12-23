# vals = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

with open('input.txt', 'r') as fh:
    vals = [int(c) for c in fh.read().split(' ')]

class Node(object):
    def __init__(self, parent=None):
        self.parent = parent
        self.num_children = None
        self.num_metadata = None
        self.child_nodes = []
        self.metadata = []

    def __str__(self):
        return f'# Children: {self.num_children} # Metadata: {self.num_metadata} Metadata: {self.metadata} Children: {[str(n) for n in self.child_nodes]}'

parent = None
node = Node()
top = node
metadata = 0
# print(f'# vals: {len(vals)}')

n = 0
loop = True
#while loop:
while n < len(vals):
    v = vals[n]
    # print(f'n: {n}, v: {v}')
    if node.num_children is None:
        node.num_children = v
        # print('set num_children')
    elif node.num_metadata is None:
        node.num_metadata = v
        # print('set num_metadata')
    elif node.num_children != len(node.child_nodes):
        parent = node
        node = Node(parent=parent)
        parent.child_nodes.append(node)
        n -= 1
        # print('set new node')
    elif node.num_metadata != len(node.metadata):
        node.metadata.append(v)
        metadata += v
        # print('append metadata')
    else:
        if node.parent:
            node = node.parent
            # print('back to parent')
            n -= 1
    n += 1
print(top)
print(metadata)
