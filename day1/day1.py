"""
Day 1 Advent of Code 2023
First task is to find two digits (first and last) from line of text and combine them into two-digit number.
Second is similar, but digits could also be hidden as words (one, two, etc.), not only as number.
"""

import os

def search_number(line_list):
    """
    First task function
    The idea is to search through every character and try to convert them into integer.
    """
    
    numbers = []                            # list with resulting numbers
    
    for line in line_list:
        charlist = list(line)
        number = 0                          # number hidden in this line
        for char in charlist:
            try:
                digit = int(char)
                if number == 0:             # check if it is first digit
                    number += 10*digit
            except ValueError:              # if char is not a number then pass
                pass
        if number != 0:                     # if line does not have hidden number
            numbers.append(number + digit)

    return sum(numbers)


def check_letters(digit, it):
    """
    Auxillary function for second task
    Checks if given list has equal elements as iterator
    """
    for letter in digit:
        try:
            if letter == next(it):
                pass
            else:
                return False
        except StopIteration:
            return False
    return True     # iterator does not have to end

def search_numberv2(line_list):
    """
    Second task function
    The idea is to search through every character and try to convert them into integer.
    If character is not an integer then function checks if next letters do not shape into spelled out digit.
    """
    
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = [list(dig) for dig in digits]
    first_letters = [digits[i][0] for i in range(len(digits))]
    numbers = []
  
    for line in line_list:
        charlist = list(line)
        number = 0
        for i, char in enumerate(charlist):
            try:
                digit = int(char)
                if number == 0:
                    number += 10*digit
            except ValueError:
                for num, letter in enumerate(first_letters):    # check if letter is interesting one
                    if char == letter:
                        it = iter(charlist)                     # iterator that consist of remaining characters
                        for n in range(i):
                            next(it)
                        if check_letters(digits[num], it) is True:  # checks if spelled out digit is hidden in iterator
                            digit = num+1
                            if number == 0:
                                number += 10*digit
                        else:
                            pass
                            
        if number != 0:
            numbers.append(number + digit)

    return sum(numbers)


# Running a function

file_path = os.path.dirname(__file__)
file_path += '\input.txt'

with open(file_path) as file:
    print(search_numberv2(file))  


       