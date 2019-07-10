# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000
# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.
# Так же при выводе имя должно быть полностью в верхнем регистре!
# Подумайте вспоминая урок, как это можно сделать максимально кратко, используя возможности языка Python.

employes_file_name = "salary.txt"

print("\nЗадача-1\n")

names_list = ["Василий", "Олег", "Татьяна", "Петр", "Андрей"]
pays_list = [25000, 610000, 30000, 41000, 38000]

employes_dict = dict(zip(names_list, pays_list))


def write_employes_dict(dict1, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for name, pay in dict1.items():
            file.write(f"{name} - {pay}\n")


def print_employes(file_name, upper_show_pay):
    with open(file_name, "r", encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            name, pay = line.split(" - ")
            name = name.upper()
            pay = float(int(pay) - int(pay) * 13 / 100)
            if pay <= upper_show_pay:
                print(f"{name} - {pay:.2f}")


print("Результирующий словарь:", employes_dict)
write_employes_dict(employes_dict, employes_file_name)
print("\nЗарплатная ведомость:")
print_employes(employes_file_name, 500000)
