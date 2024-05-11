from set_char_info import checkCharClass, makeCharTemp, checkCharName, makeSavegame

print("Create your character:")
print("Name: ")
char_name = input()
checkCharName(char_name)

print("Pick a class: ")
print("1 - Warrior | 2 - Mage | 3 - Archer")
char_class = input()
checkCharClass(char_class)
makeCharTemp(char_name, char_class)

# print("Deseja criar: ")
# print(f"[{char_name} - {checkCharClass(char_class)}]?")
# create = input()
# checkYesNo(create, makeSavegame(f'{char_name}_temp.csv', f'{char_name}'))

makeSavegame(f'{char_name}_temp.csv', f'{char_name}')