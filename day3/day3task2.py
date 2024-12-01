"""
Day 3 Advent of Code 2023
Second task is to find *-symbols adjacent to two numbers
"""

import numpy as np
import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'


def list_merger(list):
    """
    Auxillary function. Merge next numbers in list into nested list.
    [1,2,3,6,7,8] -> [[1,2,3],[6,7,8]]
    """
    newlist = []
    for i, n in enumerate(list):
        if i == 0:
            newlist.append([n])
            continue
        if n - newlist[-1][-1] == 1:
            newlist[-1].append(n)
            continue
        else:
            newlist.append([n])
            continue
    return newlist


gear_num = []       # list with gears part numbers
gear_id = 0         # gear index

with open(file_path) as file:
    for line_id, line in enumerate(file):
        line = line.replace('\n', '')           # \n remove in the end of line
        line = list(line)
        
        # setting variables in first iteration
        if line_id == 0:                        
            previous_line = ['.' for i in range(len(line))]
            previous_num_id = []
            previous_sym_id = []
            previous_fit_num_id = []
    
        num_id = []             # list with number ids in line
        sym_id = []             # list with symbol ids in line

        # appending number and symbol ids to list
        for i, elem in enumerate(line):     
            if elem == '.':
                continue
            else:
                try:
                    num = int(elem)
                    num_id.append(i)
                except ValueError:
                    if elem == '*':
                        sym_id.append(i)
                        gear_num.append([])
                    
        num_id = list_merger(num_id)            # sort list such that each number is on separete nested list
        
        for i in previous_sym_id:
            fit_num_id = [[], []]           # list with gear numbers id. [[previous line],[current line]]
            for sublist in num_id:          # lower 3 places check
                for index in sublist:
                    if i-1 == index or i == index or i+1 == index:
                        for elem in sublist:
                            fit_num_id[1].append(elem)
                        break

            fit_num_id[1] = list_merger(fit_num_id[1])
            for number in fit_num_id[1]:     # gear part number from previous line symbol
                num = 0
                for j, index in enumerate(number):
                    num += int(line[index]) * 10**(len(number)-1-j)
                gear_num[gear_id].append(num)
            gear_id += 1
        
        for i in sym_id:                    # upper 3 places check
            fit_num_id = [[], []]           # list with gear numbers id. [[previous line],[current line]]
            for sublist in previous_num_id:
                for index in sublist:
                    if i-1 == index or i == index or i+1 == index:
                        for elem in sublist:
                            fit_num_id[0].append(elem)
                        break
            for sublist in num_id:      # 2 places next to symbol check
                if i-1 == sublist[-1] or i+1 == sublist[0]:
                    for elem in sublist:
                        fit_num_id[1].append(elem)
           
            fit_num_id[0] = list_merger(fit_num_id[0])
            fit_num_id[1] = list_merger(fit_num_id[1])
            for number in fit_num_id[0]:    # gear part number from current line symbol
                num = 0
                for i, index in enumerate(number):
                    num += int(previous_line[index]) * 10**(len(number)-1-i)
                gear_num[gear_id].append(num)
            for number in fit_num_id[1]:     # gear part number from previous line symbol
                num = 0
                for j, index in enumerate(number):
                    num += int(line[index]) * 10**(len(number)-1-j)
                gear_num[gear_id].append(num)
            gear_id += 1
                    
        gear_id -= len(sym_id)  # get value index as at the start of current line
        
        # giving information about this line to next iteration
        previous_fit_num_id = fit_num_id[1]
        previous_line = line
        previous_num_id = num_id
        previous_sym_id = sym_id

sum = 0
for gear in gear_num:
    if len(gear) == 2:
        sum += np.prod(gear)
print(sum)  # printing answer
