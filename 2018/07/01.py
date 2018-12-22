with open('input.txt', 'r') as fh:
    orig_steps = [(l[5:6], l[-13:-12]) for l in fh]

# orig_steps = [('C', 'A'), ('C', 'F'), ('A', 'B'), ('A', 'D'), ('B', 'E'), ('D', 'E'), ('F', 'E')]
steps = orig_steps[:]
out = []
while steps:
    starts = set(s[0] for s in steps)
    finishes = set(s[1] for s in steps)
    s = list(starts.difference(finishes))
    s.sort()
    if s[0] not in out:
        out.append(s[0])
    steps = [i for i in steps if i[0] != s[0]] 
finishes = set(s[1] for s in orig_steps)
print(''.join(out) + list(finishes.difference(set(out)))[0])
