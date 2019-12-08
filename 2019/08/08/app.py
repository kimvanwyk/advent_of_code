WIDTH = 25
HEIGHT = 6
# WIDTH = 3
# HEIGHT = 2
LAYER_TOTAL = WIDTH * HEIGHT

# inputs = '123456789012'
# inputs = '001123123452789012'
with open('input.txt', 'r') as fh:
    inputs = fh.read().strip()

layers = []
for (n,p) in enumerate(inputs):
    if not n % LAYER_TOTAL:
        layers.append([])
    layers[-1].append(int(p))

zeroes = None
for (n,layer) in enumerate(layers):
    num = len([z for z in layer if z == 0])
    if (zeroes is None) or (num < zeroes):
        zeroes = num
        lowest = n
print('lowest:', lowest, 'zeroes:', zeroes)
print(layers[lowest])
digits = []
for d in (1,2):
    digits.append(len([i for i in layers[lowest] if i == d]))
print(digits[0] * digits[1])
