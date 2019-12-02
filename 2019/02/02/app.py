import operator

# inputs = [[1,9,10,3,2,3,11,0,99,30,40,50],
#           [1,0,0,0,99],
#           [2,3,0,3,99],
#           [2,4,4,5,99,0],
#           [1,1,1,4,99,5,6,0,99]]

with open('input.txt', 'r') as fh:
    inputs = [[int(i) for i in fh.readline().strip().split(',')],]

inputs[0][1] = 12
inputs[0][2] = 2

ops = {1: operator.add,
       2: operator.mul}

def process(inputs):
    n = 0
    while True:
        if inputs[n] == 99:
            break
        inputs[inputs[n+3]] = ops[inputs[n]](inputs[inputs[n+1]], inputs[inputs[n+2]])
        n += 4
    return inputs
    
for i in inputs:
    print(i)
    print(process(i))
    print()
