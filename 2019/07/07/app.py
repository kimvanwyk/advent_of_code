import operator

inputs = [0]

# instructions = ['3','15','3','16','1002','16','10','16','1','16','15','15','4','15','99','0','0']
# phases = [4,3,2,1,0]

# instructions = ['3','23','3','24','1002','24','10','24','1002','23','-1','23','101','5','23','23','1','24','23','23','4','23','99','0','0']
# phases = [0,1,2,3,4]

instructions = ['3','31','3','32','1002','32','10','32','1001','31','-2','31','1007','31','0','33','1002','33','7','33','1','33','31','31','1','32','31','31','4','31','99','0','0','0']
phases = [1,0,4,3,2]

# instructions = []
# with open('input.txt', 'r') as fh:
#     for l in fh:
#         instructions.extend(l.strip().split(','))

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
        if code in ops:
            print(ops[code].__name__, params[0], 'and', params[1], ', write to pos ', params[2])
            instructions[params[2]] = ops[code](params[0], params[1])
        if code == 3:
            i = inputs.pop(0)
            print(f'writing {i} to position {params[0]}')
            instructions[params[0]] = i
        if code == 4:
            i = params[0]
            print(f'outputting {i}')
            out.append(i)
        if (code in jump) and (jump[code][0](params[0], jump[code][1])):
            print(f'jumping to position {params[1]}')
            n = params[1]
        else:
            n += lengths[code] + 1
        if code in comp:
            print('checking if', params[0], comp[code].__name__, params[1], '-> Write 1 if so, 0 otherwise')
            instructions[params[2]] = 1 if comp[code](params[0], params[1]) else 0
        print()

    return (out, instructions)

orig = instructions[:]
out = [0]
for phase in phases:
    inputs = [phase, out[0]]
    (out, instructions) = process(instructions, inputs)
    print(out)
