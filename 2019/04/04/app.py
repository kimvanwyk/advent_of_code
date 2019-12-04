start = 240920
stop = 789857

# start = 100
# stop = 123

possibilities = []
n = start
while n <= stop:
    s = f"{n}"
    if all([s[j] <= s[j + 1] for j in range(len(s) - 1)]):
        ret = ''.join([str(int(s[j+1]) - int(s[j])) for j in range(len(s) - 1)])
        if '0' in ret:
            possibilities.append(n)
    n += 1
print(possibilities)
print(len(possibilities))
