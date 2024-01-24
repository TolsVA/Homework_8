from ui import start_menu
from init import init_menu
from print_data import print_file
import os

if __name__ == '__main__':
    os.system('cls')
    if os.path.exists('db/data_1.txt') == False:
        init_menu()

    # print()

    start_menu()