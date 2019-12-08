import itertools
import operator
from queue import Queue
import threading
from time import sleep

# inputs = [0]
# instructions = ['3','26','1001','26','-4','26','3','27','1002','27','2','27','1','27','26','27','4','27','1001','28','-1','28','1005','28','6','99','0','0','5']
# phases_list = [[9,8,7,6,5]]

# instructions = ['3','52','1001','52','-5','52','3','53','1','52','56','54','1007','54','5','55','1005','55','26','1001','54','-5','54','1105','1','12','1','53','54','53','1008','54','0','55','1001','55','1','55','2','53','55','53','4','53','1001','56','-1','56','1005','56','6','99','0','0','0','0','10']
# phases_list = [[9,7,8,5,6]]

instructions = []
with open('input.txt', 'r') as fh:
    for l in fh:
        instructions.extend(l.strip().split(','))
phases_list = [l for l in itertools.permutations([5,6,7,8,9])]

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
    if code in ops or code in (3,7,8):
        modes[-1] = 1
    return (code, modes)

def get_params(instructions, params, modes):
    out = []
    # print('in params: p:', params, 'm:', modes)
    for (p,m) in zip(params, modes):
        if m == 0:
            # print(instructions[int(p)])
            out.append(int(instructions[int(p)]))
        if m == 1:
            out.append(int(p))
    return out

def process(instructions, input_queue, output_queue, debug=False):
    n = 0
    out = []
    try:
        while True:
            # print(instructions[:40])
            if debug:
                print('n:', n, 'instructions n->n+10:', instructions[n:n+10])
            (code,modes) = get_modes(instructions[n])
            if code == 99:
                break
            params = get_params(instructions, instructions[n+1:n+lengths[code]+1], modes)
            if debug:
                print('c:', code, 'm:', modes, 'p:', params)
            if code in ops:
                if debug:
                    print(ops[code].__name__, params[0], 'and', params[1], ', write to pos ', params[2])
                instructions[params[2]] = ops[code](params[0], params[1])
            if code == 3:
                i = input_queue.get()
                if debug:
                    print(f'writing {i} to position {params[0]}')
                instructions[params[0]] = i
            if code == 4:
                i = params[0]
                if debug:
                    print(f'outputting {i}')
                output_queue.put(i)
            if (code in jump) and (jump[code][0](params[0], jump[code][1])):
                if debug:
                    print(f'jumping to position {params[1]}')
                n = params[1]
            else:
                n += lengths[code] + 1
            if code in comp:
                if debug:
                    print('checking if', params[0], comp[code].__name__, params[1], '-> Write 1 if so, 0 otherwise')
                instructions[params[2]] = 1 if comp[code](params[0], params[1]) else 0
            if debug:
                print()
        return
    except Exception as e:
        output_queue.put(None)
        return

vals = []
queues = (Queue(), Queue(), Queue(), Queue(), Queue())
for phases in phases_list:
    try:
        machines = []
        for (n,name) in enumerate('abcde',0):
            machines.append(threading.Thread(name=name, target=process, args=(instructions[:], queues[n-1], queues[n]), kwargs={'debug':False}))
        for m in machines:
            m.start()
        for (n,phase) in enumerate(phases):
            queues[n-1].put(phase)
        queues[-1].put(0)
        while threading.active_count() > 1:
            sleep(0.1)
        if any([q.qsize() for q in queues[:4]]):
            print('error:', [q.qsize() for q in queues[:4]])
            raise
        i = queues[-1].get()
        if i is None:
            print('None in queue 4')
            raise
        vals.append(i)
        # print([q.qsize() for q in queues])
    except Exception as e:
        continue

vals.sort(reverse=True)
print(vals)
