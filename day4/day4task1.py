"""
Day 4 Advent of Code 2023
First task is to find which numbers are the same on each side of '|'
"""

import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'

sum_win_numbers = 0      # sum of points

with open(file_path) as file:
    for card_id, card in enumerate(file):
        card = card.replace('\n', '')               # \n remove in the end of line
        card = card.split(':')
        card.pop(0)                                 # excluding needless element from memory
        card = card[0].split('|')
        card = [card[i].split(' ') for i in range(len(card))]
        
        for i in range(len(card)):                  # remove empty elemnts
            card[i] = [x for x in card[i] if x]
            
        n = 0                                       # number of winning numbers    
        for l_number in card[0]:
            for r_number in card[1]:
                if l_number == r_number:
                    n +=1
                    break                           # assumption that numbers are not duplicated
        if n > 0:
            sum_win_numbers += 2**(n-1)           
                    
                
print(sum_win_numbers)
        
