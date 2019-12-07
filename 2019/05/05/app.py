import operator

inputs = [1]

# instructions = ['1002','4','3','4','33','99']
# instructions = ['1101','100','-1','4','0']
instructions = []
with open('input.txt', 'r') as fh:
    for l in fh:
        instructions.extend(l.strip().split(','))

ops = {1: operator.add,
       2: operator.mul}

lengths = {1: 3,
           2: 3,
           3: 1,
           4: 1,
           99:1}

def get_modes(op):
    s = str(op)
    if len(s) < 2:
        s = f'0{s}'
    code = int(s[-2:])
    modes = [int(c) for c in s[:-2][::-1]]
    if len(modes) < lengths[code]:
        modes.extend([0] * (lengths[code] - len(modes)))
    if code in ops or code in (3,):
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

def process(instructions, inputs=[]):
    n = 0
    out = []
    while True:
        print(instructions[:40])
        print('n:', n, 'instructions n->n+10:', instructions[n:n+10])
        (code,modes) = get_modes(instructions[n])
        if code == 99:
            break
        params = get_params(instructions, instructions[n+1:n+lengths[code]+1], modes)
        print('c:', code, 'm:', modes, 'p:', params)
        # print(code)
        # print(modes)
        # print(params)
        if code in ops:
            print(ops[code].__name__, params[0], 'and', params[1], ', write to pos ', params[2])
            instructions[params[2]] = ops[code](params[0], params[1])
        if code == 3:
            i = inputs.pop(0)
            print(f'writing {i} to position {params[0]}')
            instructions[params[0]] = i
        if code == 4:
            i = params[0]
            print(f'reading {i} from position {params[0]}')
            out.append(i)
        n += lengths[code] + 1
        print()
        # input()

    return (out, instructions)

(out, instructions) = process(instructions, inputs)
print(instructions)
print(out)
