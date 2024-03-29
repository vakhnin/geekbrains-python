# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

print("\nЗадача-1\n")

name_re = r"^[A-ZА-ЯЁ][a-zа-яё]+$"
email_re = r"^[a-z][a-z0-9_]*@[a-z0-9]+\.(com|org|ru)$"

name = input("Введите имя:")
surname = input("Введите фамилию:")
email = input("Введите e-mail:")

if re.match(name_re, name):
    print("Имя указано верно.")
else:
    print("Имя указано не верно.")

if re.match(name_re, surname):
    print("Фамилия указана верно.")
else:
    print("Фамилия указана не верно.")

if re.match(email_re, email):
    print("E-mail указан верно.")
else:
    print("E-mail указан не верно.")


# Задача - 2:
# Вам дан текст:

some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# более одной точки, при любом исходе сообщите результат пользователю!

print("\nЗадача-2\n")

more_then_one_point_re = r"\.(\.)+"

if re.findall(more_then_one_point_re, some_str):
    print(f"Более чем одна точка подряд наедена {len(re.findall(more_then_one_point_re, some_str))} раз.")
else:
    print("В тексте не найдена более чем одна точка подряд.")
