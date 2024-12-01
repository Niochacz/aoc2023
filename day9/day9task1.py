"""
Day 9 Advent of Code 2023
Extrapolate line with some kind of Pascal's triangle
"""

import itertools as it
import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'


# function for iterating 2 neighbouring elements from list at once
# (s[0],s[1]),(s[1,s[2]]), ..., (s[n-1],s[n])
def iter2(iterable):
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)


def diff(line):
    # create list of diffrences
    new = []
    for i, j in iter2(line):
        new.append(j - i)
    return new


def ifall0(line):
    last_num = [line[-1]]   # list of last elements
    while not all(v == 0 for v in line):
        if len(line) == 1:
            return 0
        else:
            line = diff(line)
            last_num.append(line[-1])
    return sum(last_num)


def main(file_path):
    # extracting lines from file
    extra_sum = 0   # result sum
    with open(file_path) as file:
        for line in file:
            line = line.replace('\n', '')
            line = line.split(' ')
            line = [int(i) for i in line]
            extra_sum += ifall0(line)
    return extra_sum


print(main(file_path))
