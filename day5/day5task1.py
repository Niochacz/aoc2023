"""
Day 5 Advent of Code 2023
First task is to find numbers after a couple of permutation written in file as:
start of outcome range     start of input range     range number
"""

import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'

with open(file_path) as file:
    for line_id, line in enumerate(file):
        if line_id == 0:    # obtaining starting points 'seeds' from first line
            line = line.replace('\n', '')
            line = line.split(':')
            line.pop(0)
            line = line[0].split(' ')
            seed_list = [int(x) for x in line if x]
            new_seed_list = ['' for x in seed_list]
            continue
        
        if line == '\n':    # if there is an intendent (end of permutations set) overwrite starting values with permutated values
            if new_seed_list:
                for seed_id, new_seed in enumerate(new_seed_list):
                    if new_seed:
                        seed_list[seed_id] = new_seed
                new_seed_list = ['' for x in seed_list]
            continue
        
        else:
            line = line.replace('\n', '')
            line = line.split(' ')
            if line[0].isdigit():       # if line with numbers
                line = [int(x) for x in line]
                for seed_id, seed in enumerate(seed_list):
                    if seed >= line[1] and seed < line[1] + line[2]:        # if seed permutates
                        new_seed_list[seed_id] = seed - line[1] + line[0]   # new seed value
                
            else:
                continue
 
if new_seed_list:       # there is no intendent in the end, so the last one overwrite is out of loop
    for seed_id, new_seed in enumerate(new_seed_list):
        if new_seed:
            seed_list[seed_id] = new_seed
    new_seed_list = ['' for x in seed_list]            

print(min(seed_list))       