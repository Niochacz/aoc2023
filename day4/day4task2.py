"""
Day 4 Advent of Code 2023
Second task is to find number of total cards if you win copies of next i cards,
where i is quantity of winning numbers in card
"""

import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'

card_copies = [1]      # list of card copies

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
                    n += 1
                    break                           # assumption that numbers are not duplicated
                    
        if len(card_copies) == card_id:             # if there is yet no element (won copies) append 1 - original card
            card_copies.append(1)
            
        for i in range(n):                          
            if len(card_copies) < i+card_id+2:      # if there is no element append number of won copies + original one
                card_copies.append(card_copies[card_id]+1)
            else:                                   # else add won copies to list
                card_copies[i+card_id+1] += card_copies[card_id]
                                          
print(sum(card_copies))
        
