"""
Day 3 Advent of Code 2023
First task is to find numbers adjacent to some non-dots symbols
"""
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


right_numbers = []      # final list with right numbers

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
                    sym_id.append(i)
                    
        num_id = list_merger(num_id)            # sort list such that each number is on separete nested list
        fit_num_id = [[], []]                   # list with right numbers id. [[previous line],[current line]]
        
        # lower 3 places check
        for i in previous_sym_id:               
            for sublist in num_id:
                for index in sublist:
                    if i-1 == index or i == index or i+1 == index:
                        for elem in sublist:
                            fit_num_id[1].append(elem)
                        break
        
        # upper 3 places check
        for i in sym_id:               
            for sublist in previous_num_id:
                for index in sublist:
                    if i-1 == index or i == index or i+1 == index:
                        for elem in sublist:
                            fit_num_id[0].append(elem)
                        break
        
        # 2 places next to symbol check
        for i in sym_id:               
            for sublist in num_id:
                if i-1 == sublist[-1] or i+1 == sublist[0]:
                    for elem in sublist:
                        fit_num_id[1].append(elem)
        
        fit_num_id[0] = list(dict.fromkeys(fit_num_id[0]))   # eliminating same number if more than one symbol above
        fit_num_id[1] = list(dict.fromkeys(fit_num_id[1]))   # eliminating same number if more than one symbol next to or under
        
        fit_num_id[0] = list_merger(fit_num_id[0])
        fit_num_id[1] = list_merger(fit_num_id[1])

        # eliminating same number if symbols are both above and under
        for index, i in enumerate(fit_num_id[0]):   
            for j in previous_fit_num_id:
                if i == j:
                   fit_num_id[0].pop(index)

        # obtaining right number in line
        for number in fit_num_id[1]:        
            num = 0
            for i, index in enumerate(number):
                num += int(line[index]) * 10**(len(number)-1-i)
            right_numbers.append(num)
         
        # obtaining right number in previous line    
        for number in fit_num_id[0]:        
            num = 0
            for i, index in enumerate(number):
                num += int(previous_line[index]) * 10**(len(number)-1-i)
            right_numbers.append(num)
        
        # giving information about this line to next iteration
        previous_fit_num_id = fit_num_id[1]     
        previous_line = line
        previous_num_id = num_id
        previous_sym_id = sym_id
                  
print(sum(right_numbers))  # printing answer
