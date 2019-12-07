import operator

inputs = [5]

# instructions = ['1002','4','3','4','33','99']
# instructions = ['3','9','8','9','10','9','4','9','99','-1','8']
# instructions = ['3','9','7','9','10','9','4','9','99','-1','8']
# instructions = ['3','3','1108','-1','8','3','4','3','99']
# instructions = ['3','3','1107','-1','8','3','4','3','99']
# instructions = ['3','12','6','12','15','1','13','14','13','4','13','99','-1','0','1','9']
# instructions = ['3','3','1105','-1','9','1101','0','0','12','4','12','99','1']
# instructions = ['3','21','1008','21','8','20','1005','20','22','107','8','21','20','1006','20','31','1106','0','36','98','0','0','1002','21','125','20','4','20','1105','1','46','104','999','1105','1','46','1101','1000','1','20','4','20','1105','1','46','98','99']

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

(out, instructions) = process(instructions, inputs)
print(out)
