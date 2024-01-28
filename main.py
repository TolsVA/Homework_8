from ui import start_menu
from init import init_menu
import os
from folder import Folder 

if __name__ == '__main__':
    if os.path.exists('db') == False:
        os.mkdir('db')
        init_menu()

    start_menu(Folder())