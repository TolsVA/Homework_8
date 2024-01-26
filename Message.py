import os
import json

class Message():
    def __init__(self):
        self.__welcome = '\nДоброго времени суток!'
        self.__select_file = '        Выберите файл для работы:'
        self.__error = '\rОшибка, Вы ввели << >> такой команды не существует! Введите цифру от 1 до .'
        self.__select_function = '        Выберите функцию для работы с файлом:'
        self.__your_choice = f'\nВы выбрали для работы файл << >>\n'

    def show_menu_error(self, lenght, command, menu, path):
        error_txt = self.get_error().replace('<< >>', f'<< {command} >>').replace('.', lenght)
        print('\n', error_txt, '\n', self.__select_file, '\n', '\t\t', menu)

    def show_menu_welcome(self, path, menu):
        print(self.__welcome, '\n', self.__select_file, '\n', '\t\t', menu)


    def show_menu_function_choice(self, path, menu):
        choice = self.get_your_choice().replace('<< >>', f'{path}')
        # print(f'\nВы выбрали для работы файл << {path} >>\n', self.__select_function, '\n', '\t\t', menu)
        print(choice, self.__select_function, '\n', '\t\t', menu)

    def show_menu_error_fun(self, lenght, command, menu, path):
        choice = self.get_your_choice().replace('<< >>', f'{path}')
        error_txt = self.get_error().replace('<< >>', f'<< {command} >>').replace('.', lenght)
        print('\n', error_txt, choice, self.__select_function, '\n', '\t\t', menu)                                       

    def get_error(self):
        return self.__error
    
    def get_your_choice(self):
        return self.__your_choice

def exit():
    print('\nСпасибо, что воспользовались нашими услугами!\n \
    Всего доброго!\n\
        Приходите к нам ещё :)\n')