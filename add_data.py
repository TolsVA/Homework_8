from person import *
from serialize import *
import json
import os

def add_row():
    with open(f'db2/path_file.txt', 'r', encoding='utf-8') as f:
        path_file = ''.join(f.readlines())

    if os.path.splitext(path_file)[1] == '.json':
        w_json(path_file)
    elif os.path.splitext(path_file)[1] == '.txt':
        add_row_txt(path_file)

def w_json(path_file):
    person = input_person() # person
    with open(path_file, 'r', encoding='utf-8') as f:
        persons_json = json.load(f) # dict

    persons = serialize_persons(persons_json)
    persons.append(person)

    # Создаем обьект json тип словарь (dict)
    data_json = serialize_json(persons)

    # Записываем в файл my_json{i}.json
    with open(path_file, 'w', encoding='utf-8') as file:
        json.dump(data_json, file, indent = 4)



def add_row_txt(path_file):
    person = input_person()
    with open(path_file, 'r', encoding='utf-8') as f:
        now_number_row = len(f.readlines()) + 1
    person_str = f'{person.name} {person.surname} {person.date_of_birth} {person.location}'
    with open(path_file, 'a', encoding='utf-8') as file:
        file.write(f'{now_number_row} {person_str}\n')

    print("Данные успешно записаны!")

def input_person():
    return Person(
        name = input("Введите имя: "), 
        surname = input("Введите фамилию: "), 
        date_of_birth = input("Введите дату рождения: "), 
        location = input("Введите город: ")
        )