start = 240920
stop = 789857

# start = 100
# stop = 123

possibilities = []
n = start
while n <= stop:
    s = f"{n}x"
    if (all([s[j] <= s[j + 1] for j in range(len(s) - 1)])) and (
        any([((s[j] == s[j + 1]) and (s[j + 1] != s[j + 2])) for j in range(len(s) - 1)])
    ):
        possibilities.append(n)
    n += 1
print(possibilities)
print(len(possibilities))
