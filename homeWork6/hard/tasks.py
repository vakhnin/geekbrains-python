# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.

# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка

print("\nЗадача-1 и Задача-2\n")


class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class AnimalToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "animal_toy"


class CartoonToy(Toy):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.toy_type = "cartoon_toy"


toy_types = {
    "animal_toy": AnimalToy,
    "cartoon_toy": CartoonToy
}


class MakeToy:
    def __init__(self, name, color, toy_type):
        self.name = name
        self.color = color
        self.toy_type = toy_type
        self.bought_materials = False
        self.did_sewing = False
        self.did_coloring = False

    def buying_materials(self):
        self.bought_materials = True
        print("Материалы закуплены ...")

    def doing_sewing(self):
        if not self.bought_materials:
            print("Материалы не закуплены. Пошив не возможен.")
            return
        self.did_sewing = True
        print("Пошив завершен ...")

    def doing_coloring(self):
        if not self.did_sewing:
            print("Пошив не завершен. Покраска не возможна.")
            return
        self.did_coloring = True
        print("Игрушка изготовлена.")
        return toy_types[self.toy_type](self.name, self.color)


toy_fabric = MakeToy("Плюшевый медведь", "Коричневый", "animal_toy")

toy_fabric.doing_sewing()
toy_fabric.buying_materials()
toy_fabric.doing_sewing()
toy = toy_fabric.doing_coloring()

print(f"\nИзготовлена игрушка {toy.name} цвета {toy.color} класса {toy.__class__}.")
