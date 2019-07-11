# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

print("\nЗадача-1\n")

lst = [1, 2, 4, 0, -3]

new_lst = [i ** 2 for i in lst]

print("Список квадратов исходного списка:", new_lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

import random

print("\nЗадача-2\n")

fruits_lst1 = ["apple", "avocado", "fig", "grapefruit", "grapes", "kiwi", "lime", "lemon",
               "mango", "melon", "pear", "papaya", "pineapple", "peach", "plum", "watermelon"]

fruits_lst2 = ["apple", "avocado", "apricot", "banana", "fig", "grapefruit", "mango", "melon",
               "nectarine", "orange", "pear", "papaya", "pineapple", "peach", "plum", "watermelon"]


def shake_lst(lst1, count):
    for _ in range(count):
        i = random.randint(0, len(lst1)-1)
        j = random.randint(0, len(lst1)-1)
        lst1[i], lst1[j] = lst1[j], lst1[i]


# Перемешиваем списки фруктов. В условиях задачи не требовалось, но сделал.
shake_lst(fruits_lst1, 10)
print("Новый список фруктов номер 1:", fruits_lst1)
shake_lst(fruits_lst2, 10)
print("Новый список фруктов номер 2:", fruits_lst2)

result_fruits_lst = [fruit for fruit in fruits_lst1 if fruit in fruits_lst2]
print("Список фруктов, присутсвующих в обоих списках:", result_fruits_lst)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

print("\nЗадача-3\n")

lst = [12, 9, 0, -3, -4, 3, 4]
new_lst = [i for i in lst if i > 0 and (i % 3) == 0 and (i % 4) != 0]
print("Новый список:", new_lst)
