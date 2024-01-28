import os
import json
from serialize import *

def print_data(file_name):
    if os.path.splitext(file_name)[1] == '.json':
        print(f'Вывод данных из {file_name}')
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)

        list_person = serialize_persons(data)
        for i in range(len(list_person)):
            print(list_person[i].display_info(i + 1))
        return list_person

    elif os.path.splitext(file_name)[1] == '.txt':
        print(f'Вывод данных из файла {file_name}:\n')
        with open(file_name, 'r', encoding='utf-8') as file:
            data = file.readlines()
            for i in range(len(data)):
                c = data[i].split()
                pers = Person(c[1], c[2], c[3], c[4])
                print(pers.display_info(i + 1))
        return data