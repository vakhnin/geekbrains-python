# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

print("\nЗадача-1\n")

path = os.getcwd()
dirs_lst = ["dir_" + str(i) for i in range(1, 10)]


def make_dirs(dirs_lst):
    for my_dir in dirs_lst:
        if not os.path.exists(my_dir):
            try:
                os.mkdir(my_dir)
            except OSError:
                print(f"Создать директорию {my_dir} не удалось.")
            print(f"Успешно создана директория {my_dir}.")
        else:
            print(f"Дирректория {my_dir} уже существует.")


def del_dirs(dirs_lst):
    for my_dir in dirs_lst:
        if os.path.exists(my_dir):
            try:
                os.rmdir(my_dir)
            except OSError:
                print(f"Удалить директорию {my_dir} не удалось.")
            print(f"Успешно удалена директория {my_dir}.")
        else:
            print(f"Дирректория {my_dir} уже не существует.")


# Если директория, первая в списке, существует, удаляем директории из списка, если не существует, создаем.
if os.path.exists(dirs_lst[0]):
    del_dirs(dirs_lst)
else:
    make_dirs(dirs_lst)

# # Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print("\nЗадача-2\n")

exist_dirs_lst = [dr for dr in os.listdir(os.getcwd()) if os.path.isdir(dr)]

if len(exist_dirs_lst):
    print(f"В директории \"{os.getcwd()}\" есть папки:")
    for dr in exist_dirs_lst:
        print(dr)
else:
    print(f"В директории \"{os.getcwd()} \"нет папок.")

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
