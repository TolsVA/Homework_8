import json
from person import *
from serialize import *
import os
from add_data import *

def menu_read(name_fail):
    data = None
    with open(name_fail, 'r', encoding='utf-8') as file:
        if os.path.exists(name_fail) == True:
            if os.path.splitext(name_fail)[1] == '.json':
                data = json.load(file)
            elif os.path.splitext(name_fail)[1] == '.txt':
                data = file.readlines()
    return data         

def start_menu():
    menu = {}
    path = 'db/'
    l = os.listdir(path)
    for i in range(len(l)):
        menu[f'{i+1}'] = [f'{l[i]}']

    caunt = max(map(int, list(menu.keys())))
    menu_str = '\n\t\t '.join([f'{key}.\t{menu[key][0]}' for key in menu])

    welcome = ''.join(menu_read('db2/welcome.txt'))
    select_function = ''.join(menu_read('db2/choose_file.txt'))
    command = None
    while command not in menu.keys():
        if command != None:
            welcome = ''.join(menu_read('db2/errors.txt'))
        os.system('cls')
        show_menu(menu_str, welcome.replace('.', f'{caunt}'), select_function, command)
        command = input("Введите номер команды: ")
    
    os.system('cls')

    with open(f'db2/file.txt', 'w', encoding='utf-8') as file:
        file.writelines(menu[command][0])

    with open(f'db2/path.txt', 'w', encoding='utf-8') as file:
        file.writelines(path)

    menu_program()


def show_menu(menu_str, welcome, select_function, command):
    print(welcome.replace('<< >>', f'<< {command} >>'), select_function, '\n', '\t\t '+ menu_str)
    
def exit():
    print(''.join(menu_read('db2/exit.txt')))

def menu_program():
    with open(f'db2/file.txt', 'r', encoding='utf-8') as f:
        file = f'{f.readlines()[0]}'
    menu = menu_read('db2/menu_program.json')['menu']
    menu_str = '\n\t\t '.join([f'{key}. {menu[key][0].replace('_', ' ')}' for key in menu])
    select_function = ''.join(menu_read('db2/select_function.txt'))
    welcome = f'Вы выбрали для работы файл << {file} >>\n'
    command = None
    caunt = max(map(int, list(menu.keys())))
    while command not in menu.keys():
        os.system('cls')
        if command != None:
            error = ''.join(menu_read('db2/errors.txt'))
            error = error.replace('<< >>', f'<< {command} >>')
            print(error.replace('.', f'{caunt}'))
        show_menu(menu_str, welcome, select_function, command)
        command = input("Введите номер команды: ")
    
    os.system('cls')
    globals()[menu[command][1]]()


def print_file():
    path = f'{menu_read('db2/path.txt')[0]}'
    file = f'{menu_read('db2/file.txt')[0]}'

    menu = menu_read(f'{path}{file}')

    print(f'Файл << {file} >> содержит следующую информацию:')
    os.system('cls')
    
    if type(menu) == dict:
        person = str(*list(menu.keys()))
        menu = menu[person]

        for j in menu:
            menu_person = f'{person}_{j}\n\t\t ' + '\n\t\t '.join([f'{key_2}:\r{'\t' * 5}{menu[j][i][key_2]}' for i in range(len(menu[j])) for key_2 in menu[j][i]])
            print(menu_person)

    else:
        menu = ''.join(menu)
        print(menu)
    
    num = input('\nВеруться в предыдущее меню  ->  1 и Enter\n\
                 \rВернуться в главное меню    ->  2 и Enter\n\
                 \rВыйти из программы          ->  любая клавиша и Enter\n')
    
    if num == '1':
        menu_program()
    elif num == '2':
        start_menu()
    else:
        exit()