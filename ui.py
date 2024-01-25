from person import *
from serialize import *
import os
from add_data import *
# from print_data import *

def start_menu():
    path = 'db/'
    list_file = os.listdir(path)
    lenght = len(list_file)
    menu_str = '\n\t\t '.join([f'{i + 1}. \t{list_file[i]}' for i in range(lenght)])
    welcome = ''.join(menu_read('db2/welcome.txt'))
    select_function = ''.join(menu_read('db2/choose_file.txt'))
    command = None
    while command not in [str(i + 1) for i in range(lenght)]:
        if command != None:
            welcome = ''.join(menu_read('db2/errors.txt'))
        # os.system('cls')
        show_menu(menu_str, welcome.replace('.', f'{lenght}'), select_function, command)
        command = input("Введите номер команды: ") 
    
    # os.system('cls')
    path_file = f'{path}{list_file[int(command) - 1]}'
    with open(f'db2/path_file.txt', 'w', encoding='utf-8') as file:
        file.writelines(path_file)

    menu_program(path_file)       

def show_menu(menu_str, welcome, select_function, command):
    print(welcome.replace('<< >>', f'<< {command} >>'), select_function, '\n', '\t\t '+ menu_str)
    
def exit():
    print(''.join(menu_read('db2/exit.txt')))

def menu_program(path_file):
    menu = menu_read('db2/menu_program.json')['menu']
    menu_str = '\n\t\t '.join([f'{key}. {menu[key][0].replace("_", " ")}' for key in menu])
    select_function = ''.join(menu_read('db2/select_function.txt'))
    welcome = f'Вы выбрали для работы файл << {path_file} >>\n'
    command = None
    caunt = max(map(int, list(menu.keys())))
    while command not in menu.keys():
        # os.system('cls')
        if command != None:
            error = ''.join(menu_read('db2/errors.txt'))
            error = error.replace('<< >>', f'<< {command} >>')
            print(error.replace('.', f'{caunt}'))
        show_menu(menu_str, welcome, select_function, command)
        command = input("Введите номер команды: ")
    # os.system('cls')
    globals()[menu[command][1]]()

def menu_read(name_fail):
    data = None
    with open(name_fail, 'r', encoding='utf-8') as file:
        if os.path.exists(name_fail) == True:
            if os.path.splitext(name_fail)[1] == '.json':
                data = json.load(file)
            elif os.path.splitext(name_fail)[1] == '.txt':
                data = file.readlines()
    return data

def print_file(path_file = None):
    if path_file == None:
        path_file = menu_read('db2/path_file.txt')[0]
    if os.path.splitext(path_file)[1] == '.json':
        print(f'Вывод данных из {path_file}')
        with open(path_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        list_person = serialize_persons(data)
        for i in range(len(list_person)):
            print(list_person[i].display_info(i + 1))

    elif os.path.splitext(path_file)[1] == '.txt':
        print(f'Вывод данных из файла {path_file}:\n')
        with open(path_file, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for j in range(len(data)):
                list_person = data[j].split()
                person = Person(
                    list_person[1],
                    list_person[2],
                    list_person[3],
                    list_person[4]
                )
                print(person.display_info(j + 1))

    num = input('\nВеруться в предыдущее меню  ->  1 и Enter\n\
    \rВернуться в главное меню    ->  2 и Enter\n\
    \rВыйти из программы          ->  любая клавиша и Enter')

    if num == '1':
        menu_program(path_file)
    elif num == '2':
        start_menu()
    else:
        exit()