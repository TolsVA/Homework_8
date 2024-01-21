# from ui import start_menu
from init import init_menu
from print_data import print_file
import os

if __name__ == '__main__':
    if os.path.exists('db/data_1.txt') == False:
        init_menu()

    print()
    print_file()
    # start_menu()