from file import File
from Message import *
from print_data import *
from add_data import *
from command import *
from delete_data import *

folder = None
messege = Message()
file = File()
file_name = None

def start_menu(f=None):
    if f != None:
        global folder
        folder = f

    lenght = len(folder.get_list_file())
    command = get_command([str(i + 1) for i in range(lenght)], str(lenght), messege.show_menu_welcome, messege.show_menu_error, folder.get_menu()) 
    global file_name
    file_name = f'{folder.get_path()}{folder.get_list_file()[int(command) - 1]}'
    menu_program()       

def menu_program():
    menu = file.get_list_menu()
    lenght = max(map(int, list(menu.keys())))
    command = get_command(menu.keys(), str(lenght), messege.show_menu_function_choice, messege.show_menu_error_fun, file.get_menu(), file_name)
    globals()[menu[command][1]]()

def print_file():
    print_data(file_name)
    action_request()

def add_row(): 
    add_data(file_name)
    action_request()

def delete():
    s = None
    caunt = False
    while s not in ['y', 'n']:
        if caunt:
            s = input(f'Ошибка вы ввели не коректные данные: \
                    \n\t\tвведите << y >> -> если хотите удалить файл {file_name} или << n >> -> если нет : ')
        else:
            s = input(f'Вы уверены что хотите удалить файл {file_name} y/n : ')
        caunt = True
    if s == 'y':
        os.remove(file_name)
        print(f'Файл {file_name} удалён')
    
    folder.set_path('db/')
    
    action_request()
    

def change_row(): 
    print('Пока не готово')
    action_request()

def action_request():
    num = input('Веруться в предыдущее меню  ->  1 и Enter\n\
    \rВернуться в главное меню    ->  2 и Enter\n\
    \rВыйти из программы          ->  любая клавиша и Enter\n')

    if num == '1': menu_program()
    elif num == '2': start_menu()
    else: exit()

def copy_row():
    file_copy = print_data(file_name)
    length = len(file_copy)
    command = None
    while command not in [str(i + 1) for i in range(length)]:
        command = input('Введите номер записи Person_ которую вы бы хотели скопировать.')
        if command not in [str(i + 1) for i in range(length)]:
            print(f'Не коректный ввод данных введите число от 1 до {length}')

    person = file_copy[int(command)-1]
    if type(person) != Person: 
        data = person.split()
        person = Person(data[1], data[2], data[3], data[4])

    copy_str = person
    if type(person) != str:
        copy_str = f'{command} {person.name} {person.surname} {person.date_of_birth} {person.location}'

    print(f'Указанные данные\n{copy_str}скопированы в буфер обмена данных\nВыберите фал для вставки данных')
    lenght = len(folder.get_list_file())
    command2 = get_command([str(i + 1) for i in range(lenght)], str(lenght), messege.show_menu_welcome, messege.show_menu_error, folder.get_menu()) 

    recipient_file = f'{folder.get_path()}{folder.get_list_file()[int(command2) - 1]}'

    print(f'файл донор {file_name}')
    print(f'Скопированные данные ({copy_str})')   
    print(f'файл получатель {recipient_file}')

    add_data(recipient_file, person)

    s = None
    while s not in ['y', 'n']:
        s = input('Данные сохранены Удалить данные из файла донора y/n :  ')

    if s == 'y':
        delete_data(file_copy, command, file_name)