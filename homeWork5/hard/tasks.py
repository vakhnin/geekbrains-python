# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import shutil
# print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("ls - отоброжение полного пути")
    print("cp - копия файла")


def make_dir():
    if not name1:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), name1)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(name1))
    except FileExistsError:
        print('директория {} уже существует'.format(name1))


def ping():
    print("pong")


def ls():
    print(os.getcwd())


def copy_file():
    if not name1:
        print("Необходимо указать имя копируемого файла вторым параметром")
        return
    elif not name2:
        print("Необходимо указать имя файла в который копируем третьем параметром")
        return
    try:
        shutil.copy(name1, name2)
        print(f'Копия файла {name1} с именем {name2} создана')
    except FileNotFoundError:
        print(f'Файла {name1} не существует')


do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "ls": ls,
    "cp": copy_file
}

try:
    name1 = sys.argv[2]
except IndexError:
    name1 = None

try:
    name2 = sys.argv[3]
except IndexError:
    name2 = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
