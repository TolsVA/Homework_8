def get_command(my_range, lenght, f1, f2, menu, file_name=None):
    command = None
    while command not in my_range:
        if command == None:
            f1(file_name, menu)
        else:
            f2(lenght, command, menu, file_name)
            
        command = input("Введите номер команды: ") 
    return command