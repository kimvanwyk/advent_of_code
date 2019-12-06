import operator

inputs = [1]

# instructions = ['1002','4','3','4','33','99']
# instructions = ['1101','100','-1','4','0']
instructions = []
with open('input.txt', 'r') as fh:
    for l in fh:
        instructions.append(l.strip().split(','))

ops = {1: operator.add,
       2: operator.mul}

lengths = {1: 3,
           2: 3,
           3: 1,
           4: 1,
           99:1}

def get_modes(op):
    s = str(op)
    code = int(s[-2:])
    modes = [int(c) for c in s[:-2][::-1]]
    if len(modes) < lengths[code]:
        modes.extend([0] * (lengths[code] - len(modes)))
    if code in ops:
        modes[-1] = 1
    return (code, modes)

def get_params(instructions, params, modes):
    out = []
    for (p,m) in zip(params, modes):
        print(p,m)
        if m == 0:
            out.append(int(instructions[int(p)]))
        if m == 1:
            out.append(int(p))
    return out

def process(instructions, inputs=[]):
    n = 0
    out = []
    while True:
        (code,modes) = get_modes(instructions[n])
        if code == 99:
            break
        params = get_params(instructions, instructions[n+1:n+lengths[code]+1], modes)
        print(code)
        print(modes)
        print(params)
        if code in ops:
            instructions[params[2]] = ops[code](params[0], params[1])
        if code == 3:
            instructions[params[0]] = inputs.pop(0)
        if code == 4:
            out.append(instructions[params[0]])
        n += lengths[code] + 1
        
    return (out, instructions)

# print(get_modes(1002))

(out, instructions) = process(instructions, inputs)
print(instructions)
print(out)


# for noun in range(100):
#     for verb in range(100):
#         with open('input.txt', 'r') as fh:
#             inputs = [[int(i) for i in fh.readline().strip().split(',')],]
#         inputs[0][1] = noun
#         inputs[0][2] = verb
#         process(inputs[0])    
#         if inputs[0][0] == 19690720:
#             print (noun,verb,(100*noun) + verb)
