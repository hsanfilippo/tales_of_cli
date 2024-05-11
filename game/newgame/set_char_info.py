import shutil
import os

def checkCharName(c_name: str) -> str:
    while c_name.__len__() <= 1:
        print('Nome muito curto. (minimo 3 caracteres)')
        c_name = input()
    if c_name.__len__() >= 3:
        print('Nome salvo')
        return c_name

def checkCharClass(c_class: str) -> str:
    is_ok = False

    while is_ok == False:
        if c_class == '1':
            return 'Warrior'

        elif c_class == '2':
            print(f'{c_class} não disponível na versão demo. Mudando p/ Warrior.')
            return 'Warrior' # Futuro mage

        elif c_class == '3':
            print(f'{c_class} não disponível na versão demo. Mudando p/ Warrior.')
            return 'Warrior' # Futuro archer

        else:
            print('Opção inválida. Escolha uma das opções abaixo:')
            print('Pick a class: ')
            print('1 - Warrior | 2 - Mage | 3 - Archer')
            c_class = input()


def makeCharTemp(c_name: str, c_class: str):

    with open(f'{c_name}_temp.csv', 'w', encoding='utf8') as fp:
        fp.write('char_name,char_class,lvl,exp,hp,atk,def,m_atk,m_def,save_state\n')
        fp.write(f'{c_name},{checkCharClass(c_class)},1,0,100,5,3,0,1,fase 1')
    print(f'[{c_name} - {checkCharClass(c_class)} - lvl. 1] criado com sucesso. Bom jogo!')

def makeSavegame(temp_char_name: str, c_name: str):
    shutil.copyfile(src=f'../newgame/{temp_char_name}', dst=f'../save_game/{c_name}.csv')
    os.remove(f'../newgame/{temp_char_name}')

# def checkYesNo(input_str: str, func_name):
    
#     while input_str.lower() not in ['y', 's', 'n']:
#         if input_str.lower() == 's':
#             func_name
#         elif input_str.lower() == 'n':
#             print('Voltar p/ criação de personagem')
#         else:
#             print('Digite uma opção válida (s ou n)')
#             input_str = input()