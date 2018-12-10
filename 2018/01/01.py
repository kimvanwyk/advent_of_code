freq = 0
with open('input.txt', 'r') as fh:
    for l in fh:
        freq += int(l.strip())
print(freq)
