from collections import defaultdict
from datetime import datetime
from pampy import match, _
import re

class Guard(object):
    def __init__(self, ID):
        self.ID = ID
        self.awake = defaultdict(int)
        self.asleep = defaultdict(int)
        self.mins_asleep = 0

    def record(self, action, min):
        if action == 'awake':
            self.awake[min] += 1
        if action == 'asleep':
            self.asleep[min] += 1
            self.mins_asleep += 1

with open('input.txt', 'r') as fh:
    d = []
    for l in fh:
        # [1518-07-18 23:57] Guard #157 begins shift
        d.append(match(l.strip().replace('1518','2018'), re.compile('\[([0-9- :]+)\] (.*)'), lambda date, msg: (datetime.strptime(date,'%Y-%m-%d %H:%M'), msg)))
    d.sort()

guards = {}
for (date, msg) in d:
    if 'Guard' in msg:
        ID = msg.split('Guard #')[-1].split(' ')[0]
        if ID not in guards:
            guards[ID] = Guard(ID)
        action_min = 0
    else:
        if 'asleep' in msg:
            action = 'awake'
        if 'wakes' in msg:
            action = 'asleep'
        for m in range(action_min, date.minute):
            guards[ID].record(action, m)
            action_min = date.minute

freq_mins = []
for g in guards.values():
    mins = [(v,k) for (k,v) in g.asleep.items()]
    mins.sort()
    if mins:
        freq_mins.append((mins[-1][0], mins[-1][-1], g.ID))
freq_mins.sort()
print(freq_mins)
print(int(freq_mins[-1][1]) * int(freq_mins[-1][2]))
