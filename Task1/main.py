# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

import os
import random
from emoji import emojize
os.system('cls')

def check_coordinates():
    x, y = int(input()), int(input())
    while not 1 <= x <= 3 or not 1 <= y <= 3:
        print('Ошибка')
        x, y = int(input()), int(input())
    return int(x), int(y)

def get_empty_table():
    empty_table = [['x/y   1    2    3'],
                    ['  1 ', ' _ |', ' _ |', ' _ '], 
                    ['  2 ', ' _ |', ' _ |', ' _ '], 
                    ['  3 ', ' _ |', ' _ |', ' _ ']]
    for i in range(0, len(empty_table)):
        for j in range(0, len(empty_table[i])):
            print(empty_table[i][j], end=' ')
        print()
    return empty_table

def game():
    player_number = random.randint(1,2)
    x_list, y_list = [], []
    count = 1
    game_table = get_empty_table()
    while count<=9:
        print(f'Игрок {player_number} введите координаты (x, y): ', end='')
        x, y = check_coordinates()        
        x_list.append(x)
        y_list.append(y)
        move = (x,y,)
        if count>=2:
            for i in range(len(coord_list)):
                while coord_list[i] == move:
                    print('Эти координаты уже использованы, введите другие')
                    x, y = check_coordinates()
                    move = (x,y,)
        for i in range(0, len(game_table)):
            for j in range(0, len(game_table[i])):
                if i==x and j==y:
                    if player_number==1:
                        game_table[i][j] = ' X  '
                    else:
                        game_table[i][j] = ' 0  '
                print(game_table[i][j], end=' ')
            print()
        coord_list = list(zip(x_list, y_list))
        count+=1
        player_number = 3-player_number

    game_table = game_table[1:4]
    del game_table[0][0]
    del game_table[1][0]  
    del game_table[2][0]  
    return game_table

game_table = [[' _ |', ' _ |', ' _ '], 
                [' _ |', ' _ |', ' _ '], 
                [' _ |', ' _ |', ' _ ']]        
def victory_check(game_table):
    result = emojize('Ничья!')
    for i in range(len(game_table)):
        if game_table[i][0]==game_table[i][1]==game_table[i][2]:
            if game_table[i][0]==' X  ':
                result = emojize('Игрок первый выиграл!:', language='alias')
            else:
                result = emojize('Игрок второй выиграл!', language='alias')
            break    
    for j in range(len(game_table)):
        if game_table[0][j]==game_table[1][j]==game_table[2][j]:
            if game_table[0][j]==' X  ':
                result = emojize('Игрок первый выиграл!', language='alias')
            else:
                result = emojize('Игрок второй выиграл!', language='alias')
            break
    if game_table[0][0]==game_table[1][1]==game_table[2][2]:
        if game_table[0][0]==' X  ':
            result = emojize('Игрок первый выиграл!', language='alias')
        else:
            result = emojize('Игрок второй выиграл!')
    if game_table[2][0]==game_table[1][1]==game_table[0][2]:
        if game_table[1][1]==' X  ':
            result = emojize('Игрок первый выиграл!', language='alias')
        else:
            result = emojize('Игрок второй выиграл!', language='alias')

    return result
        
def main():
    print('Старт игры!')
    print()
    table_game = game()
    print(victory_check(table_game))

if __name__ == "__main__":
    main()

