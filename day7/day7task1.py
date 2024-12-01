"""
Day 7 Advent of Code 2023
Sort hands of cards by poker strength
"""

import os

def handtodict(hand):
    # Count number of duplicates in string and sort them decreasingly
    count = {i: list(hand).count(i) for i in list(hand)}
    srt = sorted(count.items(), key = lambda x: x[1], reverse = True)
    return list(dict(srt).values())


def handtointlist(hand):
    # Convert hand string to list of integers corresponding to cards strength
    new = []
    hand = list(hand)
    for el in hand:
        if el.isdigit():
            new.append(int(el))
            continue
        else:
            if el == 'T':
                new.append(10)
                continue
            if el == 'J':
                new.append(11)
                continue
            if el == 'Q':
                new.append(12)
                continue
            if el == 'K':
                new.append(13)
                continue
            if el == 'A':
                new.append(14)
                continue
    return new


def sorttype(hands):
    # Sort hands into nested list by hand type
    sorted_hands = [[], [], [], [], [], [], []]
    for hand, bid in hands:
        h_v = handtodict(hand)
        hand = handtointlist(hand)
        if h_v[0] == 5:
            sorted_hands[6].append((hand, bid))
            continue
        if h_v[0] == 4:
            sorted_hands[5].append((hand, bid))
            continue
        if h_v[0] == 3:
            if h_v[1] == 2:
                sorted_hands[4].append((hand, bid))
                continue
            sorted_hands[3].append((hand, bid))
            continue
        if h_v[0] == 2:
            if h_v[1] == 2:
                sorted_hands[2].append((hand, bid))
                continue
            sorted_hands[1].append((hand, bid))
            continue
        else:
            sorted_hands[0].append((hand, bid))
          
    return sorted_hands


def sortstrength(hands):
    # Sort nested list by card strength and flatten list
    sorted_hands = sorttype(hands)
    for l in sorted_hands:
        l.sort(key = lambda x: x[0])
    return sum(sorted_hands, [])    

def gethands(file_path):
    # Read file and create list of tuples with string hand and bid
    hands = []
    with open(file_path) as file:
        for line_id, line in enumerate(file):
            line = line.replace('\n', '')
            line = line.split(' ')
            line[1] = int(line[1])
            hands.append(line)
    return hands


def main():
    file_path = os.path.dirname(__file__)
    file_path += '\input.txt'
    sorted_hands = sortstrength(gethands(file_path))
    total = 0   # total winning number
    for i, t in enumerate(sorted_hands):
        total += (i+1) * t[1]
    print(total)    
    
main()       