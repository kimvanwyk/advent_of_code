# WORKERS = 2
# SUBT = 64
# orig_steps = [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]

with open('input.txt', 'r') as fh:
    orig_steps = [(l[5:6], l[-13:-12]) for l in fh]
WORKERS = 5
SUBT = 4

workers = [[0,'!']] * WORKERS
steps = orig_steps[:]
n = 0
done = []
while steps:
    for (j,(w,k)) in enumerate(workers):
        if w:
            w = w - 1
            workers[j][0] = w
            if not w:
                last = steps[-1]
                print('before', j, steps)
                steps = [i for i in steps if i[0] != k] 
                print('after', j, steps)
    starts = set(s[0] for s in steps)
    finishes = set(s[1] for s in steps)
    s = list(starts.difference(finishes))
    s.sort()
    s = [i for i in s if i not in done]
    print('startable', s)
    for (j,(w,k)) in enumerate(workers):
        if not w:
            if s:
                c = s.pop(0)
                workers[j] = [ord(c) - SUBT, c]
                done.append(c)
            else:
                workers[j] = [0,'!']
    if not(steps):
        for (j,(w,k)) in enumerate(workers):
            if not w:
                c = last[-1]
                if c not in done:
                    workers[j] = [ord(c) - SUBT, c]
                    steps = [(c, c)]
                    done.append(c)
    print(f'{n:03} || {workers} || {steps}')
    n += 1
print(n - 1)
