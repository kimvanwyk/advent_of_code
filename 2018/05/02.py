import string
with open('input.txt', 'r') as fh:
    orig = list(fh.read().strip())

# orig = list("dabAcCaCBAcCcaDA")
# print(orig)

def react(polymer):
    n = 0
    while n < (len(polymer)-1):
        # print(n, polymer[n], polymer[n+1])
        if abs(ord(polymer[n]) - ord(polymer[n+1])) == 32:
            #found match, skip ahead
            polymer.pop(n+1)
            polymer.pop(n)
            if n > 0:
                n -= 1
        else:
            n += 1
    # print(''.join(polymer))
    return len(polymer)

lens = []
for c in string.ascii_lowercase:
    lens.append(react([o for o in orig if o not in (c, c.upper())]))
lens.sort()
print(lens[0])
