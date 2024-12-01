import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'

with open(file_path) as file:
    power_list = []                                      # list of games power
    for game in file:
        game = game.replace('\n', '')                   # \n remove in the end of line
        spltgame = game.split(':')
        spltgame.pop(0)                                 # excluding needless element from memory
        spltgame = spltgame[0].split(';')
        for i, grab in enumerate(spltgame):
            spltgame[i] = grab.split(',')               # nested list with number and dice colour
   
        blue_num = 0
        green_num = 0
        red_num = 0
        for grab in spltgame:
            for dice in grab:
                [_, dice_num, colour] = dice.split(' ')     # obtaining number and colour of dice
                dice_num = int(dice_num)
                if colour == 'blue':                        # checking if number of dice is greater than previous
                    if dice_num > blue_num:
                        blue_num = dice_num
                        continue
                if colour == 'green':
                    if dice_num > green_num:
                        green_num = dice_num
                        continue
                if colour == 'red':
                    if dice_num > red_num:
                        red_num = dice_num
                        continue

        game_power = blue_num * green_num * red_num
        power_list.append(game_power)

print(sum(power_list))
    