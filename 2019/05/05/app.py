import operator

# inputs = [[1,9,10,3,2,3,11,0,99,30,40,50],
#           [1,0,0,0,99],
#           [2,3,0,3,99],
#           [2,4,4,5,99,0],
#           [1,1,1,4,99,5,6,0,99]]

inputs = [2]
instructions = [3,0,4,0,99]

ops = {1: operator.add,
       2: operator.mul}

lengths = {1: 3,
           2: 3,
           3: 1,
           4: 1}

def process(instructions, inputs=[]):
    n = 0
    out = []
    while True:
        op = instructions[n]
        if op == 99:
            break
        if op in ops:
            instructions[instructions[n+lengths[op]]] = ops[instructions[n]](instructions[instructions[n+1]], instructions[instructions[n+2]])
        if op == 3:
            instructions[instructions[n+1]] = inputs.pop(0)
        if op == 4:
            out.append(instructions[instructions[n+1]])
        n += lengths[op] + 1
        
    return (out, instructions)

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
