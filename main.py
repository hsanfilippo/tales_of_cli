import os

from game import newgame

def menu_check(key: str):
    if key == '1':
        os.system('clear')
        print('Iniciando novo jogo')

print('-----*--------------/\--------*-----------')
print('--------------*----/OO\-------------*-----')
print('------*-----------/0000\-------*----------')
print('# # # # # # -- TALES OF CLI -- # # # # # #')
print('# # # # # # ___   **  **   ___ # # # # # #')
print('--------------------**--------------------')
print('\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/')

print('\n------------------------------------------')
print(' 1 - NEW GAME | 2 - CONTINUE | 3 - README')
print('------------------------------------------')

print('\n               SELECT OPTION                ')

key_input = input()
menu_check(key_input)