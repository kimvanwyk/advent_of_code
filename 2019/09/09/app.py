from collections import defaultdict
import itertools
import operator
from queue import Queue
import threading
from time import sleep

# inputs = []
# instructions = ['109','1','204','-1','1001','100','1','100','1008','100','16','101','1006','101','0','99']

# inputs = []
# instructions = ['1102','34915192','34915192','7','4','7','99','0']

# inputs = []
# instructions = ['104','1125899906842624','99']

# inputs = []
# instructions = ['3','52','1001','52','-5','52','3','53','1','52','56','54','1007','54','5','55','1005','55','26','1001','54','-5','54','1105','1','12','1','53','54','53','1008','54','0','55','1001','55','1','55','2','53','55','53','4','53','1001','56','-1','56','1005','56','6','99','0','0','0','0','10']

inputs = [1]
instructions = []
with open('input.txt', 'r') as fh:
    for l in fh:
        instructions.extend(l.strip().split(','))
# phases_list = [l for l in itertools.permutations([5,6,7,8,9])]

ops = {1: operator.add,
       2: operator.mul}

lengths = {1: 3,
           2: 3,
           3: 1,
           4: 1,
           5: 2,
           6: 2,
           7: 3,
           8: 3,
           9: 1,
           99:1}

jump = {5: (operator.ne, 0),
        6: (operator.eq, 0)}

comp = {7: operator.lt,
        8: operator.eq}

def get_modes(op):
    s = str(op)
    if len(s) < 2:
        s = f'0{s}'
    code = int(s[-2:])
    modes = [int(c) for c in s[:-2][::-1]]
    if len(modes) < lengths[code]:
        modes.extend([0] * (lengths[code] - len(modes)))
    return (code, modes)

class Intcode(threading.Thread):
    def __init__(self, name, instructions, input_queue, output_queue, debug=False):
        super().__init__(name=name, daemon=True)
        self.instructions = defaultdict(int)
        for (n,i) in enumerate(instructions):
            self.instructions[n] = i
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.debug = debug
        self.relative_base = 0

    def set_params(self, positions, modes):
        out = []
        print('in params: p:', positions, 'm:', modes)
        last_different = False
        if (self.code in ops) or (self.code in comp) or (self.code in (3,)):
            last_different = True
        for (n,(pos,m)) in enumerate(zip(positions, modes),1):
            p = int(self.instructions[int(pos)])
            print(f"getting param for pos {pos}: {p}")
            if m == 2:
                p = self.relative_base + p
            if m == 1:
                out.append(int(p))
            if m in (0,2):
                if (n == len(positions)) and last_different:
                    out.append(p)
                else:
                    out.append(int(self.instructions[p]))
        self.params = out

    def run(self):
        n = 0
        out = []
        try:
            while True:
                # print(instructions[:40])
                if self.debug:
                    print(f"Thread {self.name}: ", 'n:', n, 'instructions n->n+10:', [self.instructions[j] for j in range(n,n+10)])
                (self.code,modes) = get_modes(self.instructions[n])
                if self.code == 99:
                    break
                self.set_params(list(range(n+1,n+lengths[self.code]+1)), modes)
                if self.debug:
                    print(f"Thread {self.name}: ", 'c:', self.code, 'm:', modes, 'p:', self.params)
                if self.code in ops:
                    if self.debug:
                        print(f"Thread {self.name}: ", ops[self.code].__name__, self.params[0], 'and', self.params[1], ', write to pos ', self.params[2])
                    self.instructions[self.params[2]] = ops[self.code](self.params[0], self.params[1])
                if self.code == 3:
                    i = self.input_queue.get()
                    if self.debug:
                        print(f"Thread {self.name}: ", f'writing {i} to position {self.params[0]}')
                    self.instructions[self.params[0]] = i
                if self.code == 4:
                    i = self.params[0]
                    if self.debug:
                        print(f"Thread {self.name}: ", f'outputting {i}')
                    self.output_queue.put(i)
                if self.code == 9:
                    rb = self.relative_base
                    self.relative_base += self.params[0]
                    if self.debug:
                        print(f"Thread {self.name}: ", f'Adjusting relative base from {rb} to {self.relative_base}')
                if (self.code in jump) and (jump[self.code][0](self.params[0], jump[self.code][1])):
                    if self.debug:
                        print(f"Thread {self.name}: ", f'jumping to position {self.params[1]}')
                    n = self.params[1]
                else:
                    n += lengths[self.code] + 1
                if self.code in comp:
                    if self.debug:
                        print(f"Thread {self.name}: ", 'checking if', self.params[0], comp[self.code].__name__, self.params[1], '-> Write 1 if so, 0 otherwise')
                    self.instructions[self.params[2]] = 1 if comp[self.code](self.params[0], self.params[1]) else 0
            return
        except Exception as e:
            print(f"Thread {self.name}: Exception:", e)
            self.output_queue.put(None)
            return

vals = []
queues = [Queue(), Queue()]
try:
    machines = [Intcode('a', instructions[:], queues[0], queues[1], debug=True)]
    for i in inputs:
        queues[0].put(i)
    for m in machines:
        m.start()
    while threading.active_count() > 1:
        sleep(0.1)
    if any([q.qsize() for q in queues[:-1]]):
        print('error:', [q.qsize() for q in queues[:-1]])
        raise Exception
    outputs = []
    while not queues[-1].empty():
        outputs.append(queues[-1].get())
    if None in outputs:
        print('None in final queue')
        raise Exception
    # print([q.qsize() for q in queues])
except Exception as e:
    print(e)
    pass

print(outputs)
