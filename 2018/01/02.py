freqs = {}
freq = 0
found = False
with open('input.txt', 'r') as fh:
    while True:
        for l in fh:
            freq += int(l.strip())
            if freq in freqs:
                print(freq)
                found = True
                break
            freqs[freq] = None
        fh.seek(0)
        if found:
            break
