from person import *

def serialize_json(persons):
    list_person = []
    for person in persons:
        list_person.append(
                {
                    "name": person.name, 
                    "surname": person.surname, 
                    "date_of_birth": person.date_of_birth, 
                    "location": person.location
                }
            )
    return {"persons": list_person}

def serialize_persons(persons_json):
    list_person = []
    for pers in persons_json['persons']:
        person = Person(
                name=pers['name'],
                surname=pers['surname'],
                date_of_birth=pers['date_of_birth'],
                location=pers['location']
            )
        list_person.append(person)
    return list_person