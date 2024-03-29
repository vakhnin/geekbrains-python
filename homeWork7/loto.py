#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87
      16 49    55 77    88
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""

import random


class Card:
    def __init__(self):
        self.card = self._init_card()

    @staticmethod
    def rand_elem_from_list(lst):
        return lst.pop(random.randint(0, len(lst) - 1))

    @staticmethod
    def _init_card():
        card = []
        lst = [i + 1 for i in range(90)]
        for i in range(3):
            row = []
            for j in range(5):
                row.append(Card.rand_elem_from_list(lst))
            row.sort()

            blanks_lst = [i + 1 for i in range(9)]
            for j in range(4):
                row.insert(Card.rand_elem_from_list(blanks_lst), " "*3)

            card.append(row)
        return card

    def print_card(self):
        for line in self.card:
            tmp_str = ""
            for item in line:
                if type(item) == int:
                    tmp_str += "{:>3}".format(item)
                else:
                    tmp_str += item
            print(tmp_str)


class Game:
    def __init__(self):
        self.computer_card = Card()
        self.player_card = Card()
        self.barrels = [i + 1 for i in range(90)]

    def _turn(self):
        barrel = Card.rand_elem_from_list(self.barrels)
        print(f"Новый бочонок: {barrel} (осталось {len(self.barrels)})")

        print("------ Ваша карточка -----")
        self.player_card.print_card()
        print("-" * 26)

        if barrel in self._in_one_dim_list(self.computer_card):
            self._del_number_from_card(self.computer_card, barrel)
        print("-- Карточка компьютера ---")
        self.computer_card.print_card()
        print("-" * 26)

        if input("Зачеркнуть цифру? (y/n)") == "y":
            if barrel not in self._in_one_dim_list(self.player_card):
                print("Вы проиграли.")
                return True
            else:
                self._del_number_from_card(self.player_card, barrel)
        else:
            if barrel in self._in_one_dim_list(self.player_card):
                print("Вы проиграли.")
                return True
        if self._card_full_fill(self.player_card):
            print("Вы выйграли!")
            return True
        if self._card_full_fill(self.computer_card):
            print("Вы проиграли.")
            return True

    @staticmethod
    def _in_one_dim_list(card):
        return [item for sublist in card.card for item in sublist]

    @staticmethod
    def _del_number_from_card(card1, barrel):
        card = card1.card
        for i in range(3):
            if barrel in card[i]:
                card[i][card[i].index(barrel)] = " -"
                return

    @staticmethod
    def _card_full_fill(card):
        for line in card.card:
            for item in line:
                if type(item) == int:
                    return False
        return True

    def start(self):
        while True:
            if self._turn():
                return


new_game = Game()
new_game.start()
