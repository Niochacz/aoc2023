"""
Day 5 Advent of Code 2023
Second task is to find numbers after a couple of permutation written in file as:
start of outcome range     start of input range     range number
"""

import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'


def file_processing(file_path):
    permutations = []
    with open(file_path) as file:
        for line_id, line in enumerate(file):
            if line_id == 0:    # obtaining starting points 'seeds' from first line
                line = line.replace('\n', '')
                line = line.split(':')
                line.pop(0)
                line = line[0].split(' ')
                aux_list = [int(x) for x in line if x]
                continue
            
            if line == '\n':    # if there is an indent (end of permutations set) overwrite starting values with permutated values
                permutations.append([])
                continue
            
            else:
                line = line.replace('\n', '')
                line = line.split(' ')
                if line[0].isdigit():       # if line with numbers
                    line = [int(x) for x in line]
                    permutations[-1].append(line)
                else:
                    continue
          
    #permutations.append('')
    it = iter(aux_list)
    seeds = []
    for num in it:
        seeds.append((num, next(it)))

    return seeds, permutations

def permutation(perm, seed_range):
    new = []
    for src, dst, r in perm:
        if seed_range == None:
            break
        print(src, dst, r, seed_range)
        new, seed_range = interval_check(src, dst, r, new, seed_range)
        print(seed_range)
    if not new:
        new.append(seed_range)
    return new        

def interval_check(src, dst, r, new, seed_range):
    if seed_range[0] >= dst and seed_range[0] + seed_range[1] <= dst + r:   # whole interval permutates
        new_range = (seed_range[0] - dst + src, seed_range[1])
        new.append(new_range)
        not_perm = None
    elif seed_range[0] >= dst and seed_range[0] <= dst + r and seed_range[0] + seed_range[1] > dst + r:   # left side of seed_range permutates 
        new_range = (seed_range[0] - dst + src, dst + r - seed_range[0])
        not_perm = (dst + r, seed_range[0] + seed_range[1] - r - dst)
        new.append(new_range)
    elif seed_range[0] < dst and seed_range[0] + seed_range[1] <= dst + r and seed_range[0] + seed_range[1] >= dst:   # right side of seed_range permutates 
        not_perm = (seed_range[0], dst - seed_range[0])
        new_range = (src, seed_range[0] + seed_range[1] - dst)
        new.append(new_range)
    elif seed_range[0] < dst and seed_range[0] + seed_range[1] > dst + r:     # center of seed_range permutates 
        new_range1 = (seed_range[0], dst - seed_range[0])
        new_range2 = (dst + r, seed_range[0] + seed_range[1] - r - dst)
        new_range3 = (src, r)
        not_perm = [new_range1, new_range2]
        new.append(new_range3)
    else:
        not_perm = seed_range
    return new, not_perm

def flatten(n_list):
    new = []
    for l in n_list:
        if type(l) == list:
            for e in l:
                new.append(e)
        else:
            new.append(l)
    return new         

def perm_seed(permutations, seeds):
    for perm_set in permutations:
        new_seeds = []
        print(seeds)
        for seed_range in seeds: 
            new_seeds.append(permutation(perm_set, seed_range))
        new_seeds = flatten(new_seeds)
        seeds = new_seeds
    return seeds

def min_loc_seeds(permutations, seeds):
    seeds = perm_seed(permutations, seeds)
    min_loc = 0
    for seed_range in seeds:
        if min_loc == 0:
            min_loc = seed_range[0]
            continue
        if seed_range[0] < min_loc:
            min_loc = seed_range[0]
    return min_loc         
        
        
    
    
seeds, permutations =  file_processing(file_path)
print(min_loc_seeds(permutations, seeds))



    

      