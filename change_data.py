import os
from serialize import *
import json

def change_data(file_name, index, person, file_change):
    if os.path.splitext(file_name)[1] == '.json':
        change_json(file_name, index, person, file_change)
    elif os.path.splitext(file_name)[1] == '.txt':
        change_row_txt(file_name, index, person, file_change)

def change_json(file_name, index, person, file_change): 
    file_change[index] = person
    data_json = serialize_json(file_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data_json, file, indent = 4)
    print("Данные успешно изменены!")

def change_row_txt(file_name, index, person, file_change):
    file_change[index] = f'{index +1} {person.name} {person.surname} {person.date_of_birth} {person.location}\n'
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(len(file_change)):
            file.write(f'{file_change[i]}')
    print("Данные успешно изменены!")
