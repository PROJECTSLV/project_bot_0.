# Имя файла БД. В последующем можно добавить настройки с возможностью смены файла
def file_name():
    """DATABASE . TXT"""
    return 'database.txt'


# На вход получает файл и возвращает двумерный массив
def array():
    """Full array objects: [1,2,3,4...]"""
    file1 = open(file_name())
    file1.close
    res = []
    for line in file1:
        res.append(line)
    return res

# Добавление пользователя в БД
def add_contact(id_user):
    for i in array():
        i = i.rstrip('\n')
        if i == id_user:
            return
    file1 = open(file_name(), "a+")
    file1.write(id_user + "\n")
    file1.close
