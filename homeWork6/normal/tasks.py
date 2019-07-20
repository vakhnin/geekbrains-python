# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.


class Person:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.damage = 0
        self.armor = 0

    # @staticmethod
    def _damage_on_armor(self, arm):
        return self.damage / arm

    def minus_damage(self, damage):
        self.health -= damage

    # @staticmethod
    def attack(self, person):
        person.minus_damage(self._damage_on_armor(person.armor))


class Player(Person):
    def __init__(self, name):
        self.name = name
        self.health = 110
        self.damage = 30
        self.armor = 1.3


class Enemy(Person):
    def __init__(self):
        self.name = "Enemy"
        self.health = 120
        self.damage = 25
        self.armor = 1.1


player = Player(input("Введите имя игрока:"))
enemy = Enemy()

i = 1
while True:
    if player.health < 0 or enemy.health < 0:
        break

    print(f"Раунд {i}")
    i += 1

    print(f"Атакует {player.name}")
    player.attack(enemy)
    print(f"Атакует {enemy.name}")
    enemy.attack(player)

    print(f"Здоровье {player.name}: {int(player.health)}")
    print(f"Здоровье {enemy.name}: {int(enemy.health)}\n")

if player.health > 0:
    print(f"\nПобедил игрок: {player.name}.")
elif enemy.health > 0:
    print(f"\nПобедил игрок: {enemy.name}.")
else:
    print("Оба игрока мертвы.")