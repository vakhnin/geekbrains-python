# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

print("\nЗадача-1 и Задача-2\n")


class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.speed = 0
        self.is_police = False
        self.left = "left"
        self.right = "right"

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} повернула {direction}")


class TownCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.speed = 60


class SportCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.speed = 160


class WorkCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.speed = 40


class PoliceCar(Car):
    def __init__(self, name, color):
        super().__init__(name, color)
        self.is_police = True
        self.speed = 100


car1 = SportCar("Порше", "красный")
print("Машина 1:")
print(car1.name, car1.color, car1.speed, car1.is_police)
car1.go()
car1.turn(car1.left)
car1.turn(car1.right)
car1.stop()

car2 = PoliceCar("Полицейский автомобиль", "сине-белый")
print("\nМашина 2:")
print(car2.name, car2.color, car2.speed, car2.is_police)
car2.go()
car2.turn(car2.left)
car2.turn(car2.right)
car2.stop()
