import os
from Message import *

class File():
    def __init__(self, path = 'db2/menu_program.json'):
        self.__path = path
        self.__set_menu(path)

    def __set_menu(self, path):
        self.__list_menu = menu_read(path)['menu']
        self.__menu = '\n\t\t '.join([f'{key}. {self.__list_menu[key][0].replace("_", " ")}' for key in self.__list_menu])

    def get_path(self):
        return self.__path
    
    def set_path(self, path):
        self.__path = path
        self.__set_menu(path)

    def get_menu(self):
        return self.__menu
    
    def get_list_menu(self):
        return self.__list_menu
    
def menu_read(name_fail):
    data = None
    with open(name_fail, 'r', encoding='utf-8') as file:
        if os.path.exists(name_fail) == True:
            if os.path.splitext(name_fail)[1] == '.json':
                data = json.load(file)
            elif os.path.splitext(name_fail)[1] == '.txt':
                data = file.readlines()
    return data
    
    # with open('db2/path_file.txt', 'w', encoding='utf-8') as f:
    #     f.writelines(path_file)