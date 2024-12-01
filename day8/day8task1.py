"""
Day 8 Advent of Code 2023
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
    for l in maps:            
        l.pop(0)                
    return maps


def searchmap(instr, maps):
    # iterate through instruction until ZZZ is reach
    index = 0
    it = iter(instr)
    n = 0
    while index != len(maps)-1:
        try:
            index = maps[index][next(it)]
            n += 1
        except StopIteration:
           it = iter(instr)
           continue
    return n    
    

instr, maps = getmap(file_path) 
maps.sort(key = lambda x: x[0]) # sorting map such that AAA is first and ZZZ last
maps = mapmap(maps)
print(searchmap(instr,maps)) 