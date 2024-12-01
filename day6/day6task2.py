"""
Day 6 task 2 Advent of Code 2023
Boat race. In given time count number of possibilities to beat record shown in distance.
For each second you charge (wait) boat the more velocity it gets.
"""

time = 47847467             # 71530
dist = 207139412091014      # 940200
poss = []


for i in range(1, time):
    if (time - i) * i > dist:
        poss.append(i)
        break

for i in reversed(range(1, time)):
    if (time - i) * i > dist:
        poss.append(i)
        break

print(poss)
print(poss[1] - poss[0] + 1)
