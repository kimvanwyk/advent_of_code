import re

start = 240920
stop = 789857

# start = 11000
# stop = 11423

pat = re.compile('00+')
possibilities = []
n = start
while n <= stop:
    s = f"{n}"
    if all([s[j] <= s[j + 1] for j in range(len(s) - 1)]):
        ret = ''.join([str(int(s[j+1]) - int(s[j])) for j in range(len(s) - 1)])
        if '0' in pat.sub('', ret):
            possibilities.append(n)
    n += 1
print(possibilities)
print(len(possibilities))
