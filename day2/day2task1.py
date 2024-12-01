import os

file_path = os.path.dirname(__file__)
file_path += '\input.txt'

red_num = 12
green_num = 13
blue_num = 14


with open(file_path) as file:
    game_list = []                                      # list of possible games
    for game in file:
        game = game.replace('\n', '')                   # \n remove in the end of line
        spltgame = game.split(':')
        game_num = int(spltgame[0].split(' ')[1])       # obtaining game number
        spltgame.pop(0)                                 # excluding needless element from memory
        spltgame = spltgame[0].split(';')
        for i, grab in enumerate(spltgame):
            spltgame[i] = grab.split(',')               # nested list with number and dice colour
   
        for grab in spltgame:
            for dice in grab:
                [_, dice_num, colour] = dice.split(' ')     # obtaining number and colour of dice
                dice_num = int(dice_num)
                if colour == 'blue':                        # checking if number of dice is possible
                    if dice_num <= blue_num:
                        continue
                    else:
                        break
                if colour == 'green':
                    if dice_num <= green_num:
                        continue
                    else:
                        break
                if colour == 'red':
                    if dice_num <= red_num:
                        continue
                    else:
                        break
            else:                                           # if everything is all right (no break) then continue
                continue
            break
        else:
            game_list.append(game_num)

print(sum(game_list))
    