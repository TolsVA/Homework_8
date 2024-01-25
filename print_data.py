# import json
# from serialize import *
# import os

# def menu_read(name_fail):
#     data = None
#     with open(name_fail, 'r', encoding='utf-8') as file:
#         if os.path.exists(name_fail) == True:
#             if os.path.splitext(name_fail)[1] == '.json':
#                 data = json.load(file)
#             elif os.path.splitext(name_fail)[1] == '.txt':
#                 data = file.readlines()
#     return data

# def print_file(path_file = None):
#     if path_file == None:
#         path_file = menu_read('db2/path_file.txt')[0]
#     if os.path.splitext(path_file)[1] == '.json':
#         print(f'Вывод данных из {path_file}')
#         with open(path_file, 'r', encoding='utf-8') as file:
#             data = json.load(file)

#         list_person = serialize_persons(data)
#         for i in range(len(list_person)):
#             print(list_person[i].display_info(i + 1))

#     elif os.path.splitext(path_file)[1] == '.txt':
#         print(f'Вывод данных из файла {path_file}:\n')
#         with open(path_file, 'r', encoding='utf-8') as file:
#             data = file.readlines()
#             for j in range(len(data)):
#                 list_person = data[j].split()
#                 person = Person(
#                     list_person[1],
#                     list_person[2],
#                     list_person[3],
#                     list_person[4]
#                 )
#                 print(person.display_info(j + 1))

#     num = input('\nВеруться в предыдущее меню  ->  1 и Enter\n\
#     \rВернуться в главное меню    ->  2 и Enter\n\
#     \rВыйти из программы          ->  любая клавиша и Enter\n')

#     # if num == '1':
#     #     # menu_program(path_file)
#     #     print()
#     # elif num == '2':
#     #     start_menu()
#     # else:
#     #     exit()