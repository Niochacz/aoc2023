"""
Day 10 Advent of Code 2023
Walk throuh pipeline and find how big is loop
"""

import numpy as np
import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'

M = np.loadtxt(file_path, dtype = str)  # pipeline map


def addtup(x, y):
    z = []
    for i in range(len(x)):
        z.append(x[i]+y[i])
    return tuple(z)


def fromleft(el):
    if el == '-':
        return (0, 1)
    if el == 'J':
        return (-1, 0)
    if el == '7':
        return (1, 0)
    return (0, 0)


def fromright(el):
    if el == '-':
        return (0, -1)
    if el == 'L':
        return (-1, 0)
    if el == 'F':
        return (1, 0)
    return (0, 0)


def fromtop(el):
    if el == '|':
        return (1, 0)
    if el == 'L':
        return (0, 1)
    if el == 'J':
        return (0, -1)
    return (0, 0)


def frombottom(el):
    if el == '|':
        return (-1, 0)
    if el == 'F':
        return (0, 1)
    if el == '7':
        return (0, -1)
    return (0, 0)


def walk(M, start):
    point = start
    diff = (0, 1)
    point = addtup(point, diff)
    n = 1
    while point != start:
        el = M[point[0]][point[1]]
        if diff[0] == 0:
            if diff[1] == 1:
                diff = fromleft(el)
            else:
                diff = fromright(el)
        else:
            if diff[0] == 1:
                diff = fromtop(el)
            else:
                diff = frombottom(el)
        point = addtup(point, diff)
        n += 1
    return n


for i, line in enumerate(M):
    for j, el in enumerate(line):
        if el == 'S':
            start = (i, j)


print(walk(M, start)/2)
