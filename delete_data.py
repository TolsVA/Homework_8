import os

def delete_data(file_copy, command, file_name):
    for  i in range(len(file_copy)):
        person = file_copy[i].split()
        if person[0] == command:
            file_copy.pop(i)

    if os.path.splitext(file_name)[1] == '.txt':
        with open(file_name, 'w', encoding='utf-8') as f:
            f.writelines(file_copy)