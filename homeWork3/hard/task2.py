# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

print("\nЗадача-2\n")

player_field_type = {
    "name":   "str",
    "health": "int",
    "damage": "int",
    "armor": "float"
}

player1 = {
    "name":   "player1",
    "health": 110,
    "damage": 80,
    "armor": 1.2
}

player2 = {
    "name":   "player2",
    "health": 100,
    "damage": 85,
    "armor": 1.1
}


def write_player(player):
    res_arr = []
    for key in player:
        res_arr.append(f"{key}:{player[key]}")

    with open(player["name"] + ".txt", "w", encoding='utf-8') as file:
        file.write(",".join(res_arr))


def read_player(name, fields_type):
    with open(f"{name}.txt", "r", encoding='utf-8') as file:
        player = {}
        for field in file.read().split(","):
            key, value = field.split(":")
            if fields_type[key] == "int":
                player[key] = int(value)
            elif fields_type[key] == "float":
                player[key] = float(value)
            else:
                player[key] = value

        return player


def attack(person1, person2):
    def damage_on_armor(arm, dam):
        return dam / arm
    person2["health"] -= damage_on_armor(person1["damage"], person2["damage"])


write_player(player1)
write_player(player2)
player1 = read_player("player1", player_field_type)
player2 = read_player("player2", player_field_type)

print("Бой начался!")
while player1["health"] > 0 and player2["health"] > 0:
    attack(player1, player2)
    print(f"Игрок {player1['name']} нанес удар!")
    attack(player2, player1)
    print(f"Игрок {player2['name']} нанес удар!")
    print(f"Здоровье игрока {player1['name']}:", player1["health"])
    print(f"Здоровье игрока {player2['name']}:", player2["health"])

if player1["health"] > 0:
    print(f"\nПобедил игрок: {player1['name']}.")
elif player2["health"] > 0:
    print(f"\nПобедил игрок: {player2['name']}.")
else:
    print("Оба игрока мертвы.")
