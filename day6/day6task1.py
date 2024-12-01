"""
Day 6 Advent of Code 2023
Boat race. In given time count number of possibilities to beat record shown in distance.
For each second you charge (wait) boat the more velocity it gets.
"""

from numpy import prod


time = [47, 84, 74, 67]
dist = [207, 1394, 1209, 1014]
poss = []

for t, d in zip(time, dist):
    n = 0
    for i in range(1, t):
        if (t - i) * i > d:
            n += 1
    poss.append(n)

print(poss)
print(prod(poss))
