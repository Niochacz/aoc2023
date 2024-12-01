"""
Day 8 task 2 Advent of Code 2023
Follow map with instuctions
"""

import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'


def getmap(file_path):
    # extracting instruction and map from file
    with open(file_path) as file:
        instr = list(next(file))[:-1]
        next(file)
        maps = []
        for line in file:
            for c in '\n ()':
                line = line.replace(c, '')
            line = line.split('=')
            line += line[1].split(',')
            line.pop(1)
            maps.append(line)
    for i, side in enumerate(instr):
        if side == 'L':
            instr[i] = 0
        else:
            instr[i] = 1
    return instr, maps


def mapmap(maps):
    # turning each string into indices that correspond to such string in sorted map
    for i, l in enumerate(maps):
        for m in maps:
            for ind, el in enumerate(m[1:]):
                if l[0] == el:
                    m[ind + 1] = i
    starts = start_points(maps)     # list of starting points indeces
    ends = end_points(maps)         # list of ending points indices
    for l in maps:
        l.pop(0)
    return maps, starts, ends


def start_points(maps):
    # list of starting points indeces
    starts = []
    for index, m in enumerate(maps):
        if m[0][-1] == 'A':
            starts.append(index)
    return starts


def end_points(maps):
    # list of ending points indices
    ends = []
    for index, m in enumerate(maps):
        if m[0][-1] == 'Z':
            ends.append(index)
    return ends


def searchmap(instr, maps, start, ends):
    # iterate through instruction until loop is reach
    it = iter(instr)
    index = maps[start][next(it)]
    n = 0
    ns = []
    visited_ends = []
    while index != start and index not in visited_ends:     # loop points can be start or end point
        if index in ends:
            ns.append(n)
            visited_ends.append(index)
        try:
            index = maps[index][next(it)]
            n += 1
        except StopIteration:
            it = iter(instr)
            index = maps[index][next(it)]
            n += 1
    ns.append(n)
    # apparently all loops are from next of starting to first end point
    # so only length of this one loop is needed
    return ns[1]-ns[0]
       

def searchmaploop(instr, maps, starts, ends):
    # Gathering all loop lengths
    n = []
    for start in starts:
        n.append(searchmap(instr, maps, start, ends))
    return n


def compute_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm


def loop_lengths(file_path):
    instr, maps = getmap(file_path)     # gathering data from file
    maps.sort(key = lambda x: x[0])     # sorting map such that AAA is first and ZZZ last
    maps, starts, ends = mapmap(maps)   # turning strings into indeces
    loops = searchmaploop(instr, maps, starts, ends)    # searching for loops
    return loops


# final lcm computation
loops = loop_lengths(file_path)
lcm = compute_lcm(loops[0], loops[1])
for loop in loops[2:]:
    lcm = compute_lcm(loop, lcm)
    
print(lcm)
