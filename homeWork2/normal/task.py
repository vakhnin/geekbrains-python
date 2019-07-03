# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

print("\nЗадача-1\n")

numArr = [2, -5, 8, 9, -25, 25, 4]
resArr = []
for num in numArr:
    if num >= 0:
        sqrtNum = math.sqrt(num)
        if sqrtNum == int(sqrtNum):
            resArr.append(int(sqrtNum))

print("Массив круглых корней: ", resArr)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

print("\nЗадача-2\n")

days = ("первое",
        "второе",
        "третье",
        "четвертое",
        "пятое",
        "шестое",
        "седьмое",
        "восьмое",
        "девятое",
        "десятое",
        "одиннадцатое",
        "двенадцатое",
        "тренадцатое",
        "четырнадцатое",
        "пятнадцатое",
        "шестнадцатое",
        "семьнадцатое",
        "восемьнадцатое",
        "девятнадцатое",
        "двадцатое")

months = ("января",
          "февраля",
          "марта",
          "апреля",
          "мая",
          "июня",
          "июля",
          "августа",
          "сентября",
          "октября",
          "ноября",
          "декабря")

datesArr = ("02.11.2013", "20.05.2000", "21.01.2007", "23.03.1999", "29.12.2010", "31.12.2011", "30.10.2015")

for date in datesArr:
    if len(date.split(".")) != 3:
        print("Ошибка во входных данных: ", date)
        break

    day, month, year = date.split(".")
    day = int(day) - 1
    month = int(month) - 1

    if day < 20:
        dayStr = days[day]
    elif day < 29:
        dayStr = "двадцать " + days[day - 20]
    elif day == 29:
        dayStr = "тридцатое"
    elif day == 30:
        dayStr = "тридцать первое"
    else:
        print("Ошибка во входных данных: ", date)
        break

    print(f"{date}: {dayStr} {months[month]} {year} года")


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

print("\nЗадача-3\n")

n = 15
randNumbersArr = []

for _ in range(n):
    randNumbersArr.append(random.randint(-100, 100))

print(randNumbersArr)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

print("\nЗадача-4\n")

lst = [1, 2, 4, 5, 6, 2, 5, 2]

print("Элементы списка, без повторов:")
print(set(lst))

notDoubleItemsArr = []
for item in set(lst):
    if lst.count(item) == 1:
        notDoubleItemsArr.append(item)

print("Элементы списка, которые не имеют повторений:")
print(notDoubleItemsArr)
