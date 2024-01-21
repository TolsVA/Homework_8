import json
from person import *
from serialize import *
    # 1;Семен;Семенов;02.02.2002;Тверь

    # 1;Иван;Иванов;15.01.2000;Москва
    # 2;Иван;Сидоров;1.04.2003;Москва
    # 3;Иван;Иванов;01.02.2002;Санкт-Петербург

def init_menu():
    list_persons = [
        [
            Person('Семен', 'Семенов', '02.02.2002', 'Санкт-Петербург'), 
        ], [ 
            Person('Иван', 'Иванов', '1.04.2003', 'Новосибирск'),
            Person('Пётр', 'Петров', '21.08.1998', 'Новосибирск'),
            Person('Василий', 'Васечкин', '18.11.1989', 'Новосибирск')
        ]
    ]


    for i in range(len(list_persons)):
        # Создаем обьект json тип словарь (dict)
        data_json = serialize_json(list_persons[i])

        # Записываем в файл data_file.json
        with open(f'db/my_json_{i+1}.json', 'w', encoding='utf-8') as file:
            json.dump(data_json, file, indent = 4)

        persons = []
        for person in list_persons[i]:
            list_1 = [person.name, person.surname, person.date_of_birth, person.location]
            persons.append(' '.join(list_1))  

        with open(f'db/data_{i+1}.txt', 'w', encoding='utf-8') as file:
            for i in range(len(persons)):
                file.write(f'{i+1} {persons[i]}\n')

        # json_string = json.dumps(data, indent = 4) # Переводит json в строку
        # json_type = json.loads(json_string) # Переводит строку в обьект json