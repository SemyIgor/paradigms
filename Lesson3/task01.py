""" Условие задачи
● Контекст
Вероятнее всего, вы с детства знакомы с этой игрой. Пришло 
время реализовать её. Два игрока по очереди ставят крестики 
и нолики на игровое поле. Игра завершается когда кто-то 
победил, либо наступила ничья, либо игроки отказались 
играть.

● Задача
Написать игру в “Крестики-нолики”. Можете использовать 
любые парадигмы, которые посчитаете наиболее 
подходящими. Можете реализовать доску как угодно - как 
одномерный массив или двумерный массив (массив массивов). 
Можете использовать как правила, так и хардкод, на своё 
усмотрение. Главное, чтобы в игру можно было поиграть через 
терминал с вашего компьютера. 
"""
# Создайте программу для игры в "Крестики-нолики".

import sys

# all_field = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
all_field = {
    0: '⚐ ', 1: '⚐ ', 2: '⚐ ', 3: '⚐ ', 4: '⚐ ', 5: '⚐ ', 6: '⚐ ', 7: '⚐ ', 8: '⚐ '
}

indexes = {
    '00': 0, '01': 1, '02': 2, '10': 3, '11': 4, '12': 5, '20': 6, '21': 7, '22': 8
}


def prnt_fields(field):  # Вывод игрового поля
    print(field[0], field[1], field[2])
    print(field[3], field[4], field[5])
    print(field[6], field[7], field[8])


def x_move():
    x_turn = input('Ход "крестиков". Введите код поля:')
    if x_turn not in indexes:
        return False
    all_field[indexes[x_turn]] = 'X '
    indexes.pop(x_turn)  # Удаляем поле из словаря
    prnt_fields(all_field)
    return True


print('Нумерация полей:')
for i in range(3):
    for j in range(3):
        print(str(i) + str(j), end=' ')
    print('')

try:
    if not x_move():
        sys.exit()

except:
    print('Невозможно !')

else:
    o_turn = input('Ход "ноликов". Введите код поля:')
    all_field[indexes[o_turn]] = 'O '
    prnt_fields(all_field)

# x_turn = input('Ход "крестиков". Введите код поля:')
# all_field[indexes[x_turn]] = 'X '
# indexes.pop(x_turn) # Удаляем поле из словаря
# prnt_fields(all_field)


# x_turn = input('Ход крестиков. Введите номер поля для Х: ')
# print(x_turn)
