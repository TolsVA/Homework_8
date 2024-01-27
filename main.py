from ui import start_menu
from init import init_menu
import os
from folder import Folder 

if __name__ == '__main__':
    if os.path.exists('db/data_1.txt') == False:
        init_menu()

    start_menu(Folder())