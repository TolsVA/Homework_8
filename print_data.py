import json
from serialize import *
# indent = 4
def print_file():
    for i in range(1, 3):
        with open(f'db/data_{i}.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
        print(f'Вывод данных из файла db/data_{i}.txt:\n\t'
              f'{'\t'.join(data)}')

        print(f'Вывод данных из файла db/my_json_{i}.json')
        with open(f'db/my_json_{i}.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        list_person = serialize_persons(data)

        for i in range(len(list_person)):
            print(list_person[i].display_info(i + 1))