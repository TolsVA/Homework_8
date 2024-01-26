import os

class Folder():
    def __init__(self, path = 'db/'):
        self.__path = path
        self.__set_menu(path)

    def __set_menu(self, path):
        self.__list_file = os.listdir(path) # [db/data_1.txt, db/data_2.txt, db/my_json_1.json, db/my_json_2.json]
        self.__menu = '\n\t\t '.join([f'{i + 1}.\t{self.__list_file[i]}' for i in range(len(self.__list_file))])

    def set_path(self, path):
        self.__path = path
        self.__set_menu(path)

    def get_path(self):
        return self.__path
    
    def get_list_file(self):
        return self.__list_file
    
    def get_menu(self):
        return self.__menu