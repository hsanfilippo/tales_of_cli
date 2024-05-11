char_name = 'Nezuxu'
char_class = 'Warrior'

def checkCharName(c_name: str) -> str:
    if c_name.__len__() <= 1:
        print('Nome muito curto. (minimo 3 caracteres)')
    else:
        print('Nome salvo')
        return c_name

def checkCharClass(c_class: str) -> str:
    is_ok = False

    while is_ok == False:
        if c_class == '1':
            c_class = 'Warrior'
            return c_class

        elif c_class == '2':
            c_class = 'Mage'
            print(f'{c_class} não disponível na versão demo. Mudando p/ Warrior.')
            c_class = 'Warrior'
            return c_class

        elif c_class == '3':
            c_class = 'Archer'
            print(f'{c_class} não disponível na versão demo. Mudando p/ Warrior.')
            c_class = 'Warrior'
            return c_class

        else:
            print('Opção inválida. Escolha uma das opções abaixo:')
            print('Pick a class: ')
            print('1 - Warrior | 2 - Mage | 3 - Archer')
            c_class = input()


def setCharInfo(c_name: str, c_class: str):
    print(f'{c_name}, {c_class} criado com sucesso! Bom jogo!')
    with open(f'{char_name}.txt', 'w', encoding='utf8') as fp:
        fp.write('char_name,char_class,lvl,exp,hp,atk,def,m_atk,m_def\n')
        fp.write(f'{char_name},{char_class},1,0,100,5,3,0,1')


# checkCharName(char_name)
# checkCharClass(char_class)
setCharInfo(checkCharName(char_name), checkCharClass(char_class))