"""
Day 10 Advent of Code 2023
Walk throuh pipeline and find how many tiles are enclosed by loop
"""

import itertools as it
import numpy as np
import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'

M = np.loadtxt(file_path, dtype = str)  # pipeline map


# function for iterating 2 neighbouring elements from list at once
# (s[0],s[1]),(s[1,s[2]]), ..., (s[n-1],s[n])
def iter2(iterable):
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)


def addtup(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]+y[i])
    return tuple(z)


def fromleft(el):
    if el == '-':
        return (0, 1), (0,)
    if el == 'J':
        return (-1, 0), (1,)
    if el == '7':
        return (1, 0), (1,)
    return (0, 0), (0,)


def fromright(el):
    if el == '-':
        return (0, -1), (0,)
    if el == 'L':
        return (-1, 0), (1,)
    if el == 'F':
        return (1, 0), (1,)
    return (0, 0), (0,)


def fromtop(el):
    if el == '|':
        return (1, 0), (0,)
    if el == 'L':
        return (0, 1), (1,)
    if el == 'J':
        return (0, -1), (1,)
    return (0, 0), (0,)


def frombottom(el):
    if el == '|':
        return (-1, 0), (0,)
    if el == 'F':
        return (0, 1), (1,)
    if el == '7':
        return (0, -1), (1,)
    return (0, 0), (0,)


def walk(M, start):
    point = start
    diff = (0, 1)
    point = addtup(point, diff)
    loop = []
    while point != start:
        el = M[point[0]][point[1]]
        if diff[0] == 0:
            if diff[1] == 1:
                diff, conn = fromleft(el)
            else:
                diff, conn = fromright(el)
        else:
            if diff[0] == 1:
                diff, conn = fromtop(el)
            else:
                diff, conn = frombottom(el)
        loop.append(point+conn)
        point = addtup(point, diff)
    loop.append(point+(1,))    
    loop.sort()
    return loop


def enclosed(loop):
    in_loop = True
    encl_num = 0
    for (i, j, k), (n, m, o) in iter2(loop):
        if i != n:
            in_loop = True
            continue
        if in_loop:
            print((i, j, k), (n, m, o))
            encl_num += m - j - 1
        if o == 1:
            in_loop = not in_loop
    return encl_num

for i, line in enumerate(M):
    for j, el in enumerate(line):
        if el == 'S':
            start = (i, j)


loop = walk(M, start)
print(enclosed(loop))
