NODE = 1

# vals = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
# vals = [2, 1, 1, 0, 1, 1, 0, 1, 3, 1, 0, 1, 1, 1]

with open('input.txt', 'r') as fh:
    vals = [int(c) for c in fh.read().split(' ')]

class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.num_children = None
        self.num_metadata = None
        self.child_nodes = []
        self.metadata = []
        self.val = 0
        self.md = 0
        
    def __str__(self):
        return f'{self.name:04} # Children: {self.num_children} # Metadata: {self.num_metadata} Metadata: {self.metadata} Children: {[str(n) for n in self.child_nodes]}'

    def get_val(self):
        if not self.child_nodes:
            self.val = sum(self.metadata)
            # print(f'{self.name:004} only refs: {self.val}')
        else:
            for r in self.metadata:
                r -= 1
                if 0 <= r < len(self.child_nodes):
                    # print(self.child_nodes[r])
                    self.val += self.child_nodes[r].get_val()
                    #print(f'{self.name:004} r ({r}) valid for child list. self.val: {self.val}')
                #else:
                    #print(f'{self.name:004} r ({r}) not valid for child list')
        return self.val

    def get_metadata_sum(self):
        self.md = sum(self.metadata)
        if not self.child_nodes:
            self.md = sum(self.metadata)
        else:
            for n in self.child_nodes:
                self.md += n.get_metadata_sum()
        return self.md
    

parent = None
node = Node(NODE)
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
        NODE += 1
        node = Node(NODE, parent=parent)
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
print(top.get_metadata_sum())
print(top.get_val())
