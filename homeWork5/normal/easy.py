import os


def cwd():
    return os.getcwd()


def show_dir(cur_dir):
    lst = [item for item in os.listdir(cur_dir)]

    if len(lst) == 0:
        print(f"Директория {cur_dir} пуста.\n")
        return
    for item in os.listdir(cur_dir):
        if os.path.isfile(item):
            print(f"f: {item}")
        else:
            print(f"d: {item}")


def make_dir(name_dir):
    try:
        os.mkdir(name_dir)
    except OSError:
        print(f"Не удалось создать {name_dir}")
    else:
        print(f"Успешно создана директория {name_dir}")


def del_dir(name_dir):
    try:
        os.rmdir(name_dir)
    except OSError:
        print(f"Не удалось удалить {name_dir}")
    else:
        print(f"Успешно удалена директория {name_dir}")


def change_dir(name_dir):
    try:
        os.chdir(name_dir)
    except OSError:
        print(f"Не удалось перейти в {name_dir}")
    else:
        print(f"Успешно перешли в {name_dir}")
