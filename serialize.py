from person import *

def serialize_json(persons):
    dict_persons = {}
    for i in range(len(persons)):
        dict_persons[f"{i + 1}"] = {
            'name': persons[i].name, 
            'surname': persons[i].surname,
            'date_of_birth': persons[i].date_of_birth,
            'location': persons[i].location
            }
    return {'persons': dict_persons}

def serialize_persons(persons_json):
    list_person = []
    caunt = 0
    for dic in persons_json['persons'].values():
        person = Person(
        name = dic['name'],
        surname = dic['surname'],
        date_of_birth = dic['date_of_birth'],
        location = dic['location'])
        list_person.append(person)
    return list_person
        
# def serialize_persons(persons_json):
#     list_person = []
#     for pers in persons_json['persons']:
#         person = Person(
#                 name=pers['name'],
#                 surname=pers['surname'],
#                 date_of_birth=pers['date_of_birth'],
#                 location=pers['location']
#             )
#         list_person.append(person)
#     return list_person