WIDTH = 25
HEIGHT = 6
# WIDTH = 3
# HEIGHT = 2
LAYER_TOTAL = WIDTH * HEIGHT

# inputs = '012120201010'
with open('input.txt', 'r') as fh:
    inputs = fh.read().strip()

layers = []
for (n,p) in enumerate(inputs):
    if not n % LAYER_TOTAL:
        layers.append([])
    layers[-1].append(int(p))

print(layers)
image = []
for n in range(LAYER_TOTAL):
    image.append(2)
    for layer in layers:
        if layer[n] < image[n]:
            image[n] = layer[n]
            break
print(image)

colours = {0: 'black', 1: 'white', 2: 'red'}
n = 0
with open('out.html', 'w') as fh:
    fh.write("<html><body>\n<table border='1'><tr>\n")
    for (n,p) in enumerate(image):
        if not n % WIDTH:
            fh.write('</tr><tr>')
        fh.write((f"<td width='10px' height='10px' bgcolor='{colours[p]}'></td>"))
    fh.write('</tr></table></body></html>')
    
