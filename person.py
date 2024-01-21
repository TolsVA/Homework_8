class Person():
    def __init__(self, name, surname, date_of_birth, location):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.location = location

    def display_info(self, number):
        return f'\tPerson_{number}:'+'{\n'+f' \
                    имя:              {self.name}\n \
                    фамилия:          {self.surname}\n \
                    дата рождения:    {self.date_of_birth}\n \
                    место жительства: {self.location}\n'+'\t\t }\n'