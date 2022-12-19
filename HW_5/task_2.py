"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""
from random import randint

import Methods

def player_vs_stupid_bot ():
    name_player = input('Введите свое имя: ')
    candies = 2021
    max_move = 28
    count_for_check_win = candies // max_move
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = Methods.move_player(name_player, candies, max_move)
        else:
            candies = Methods.move_stupid_bot(candies, max_move)
        if determing_moves >= count_for_check_win - 1:
            temp = Methods.check_win(candies, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1

def player_vs_smart_bot ():
    name_player = input('Введите свое имя: ')
    candies = 2021
    max_move = 28
    count_for_check_win = candies // max_move
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = Methods.move_player(name_player, candies, max_move)
        else:
            candies = Methods.move_smart_bot(candies, max_move)
        if determing_moves >= count_for_check_win - 1:
            temp = Methods.check_win(candies, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1

def player_vs_player ():
    name_first_player = input('Введите имя первого игрока: ')
    name_second_player = input('Введите имя второго игрока: ')
    candies = 2021
    max_move = 28
    count_for_check_win = candies // max_move
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = Methods.move_player(name_first_player, candies, max_move)
        else:
            candies = Methods.move_player(name_second_player, candies, max_move)
        if determing_moves >= count_for_check_win - 1:
            temp = Methods.check_win(candies, determing_moves, name_first_player, name_second_player)
            if temp:
                print(f'{temp} выиграл(а)')
                win = True
        determing_moves += 1
