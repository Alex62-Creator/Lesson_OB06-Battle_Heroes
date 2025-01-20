# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать план проекта по
# этапам/или создать kanban доску для работы над данным проектом
# Общее описание:
# Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями с различными характеристиками. Игра состоит
# из раундов, в каждом раунде игроки по очереди наносят урон друг другу, пока у одного из героев не закончится здоровье.
# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
# Классы:
# Класс Hero:
# Атрибуты:
# Имя (name)
# Здоровье (health), начальное значение 100
# Сила удара (attack_power), начальное значение 20
# Методы:
# attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# Класс Game:
# Атрибуты:
# Игрок (player), экземпляр класса Hero
# Компьютер (computer), экземпляр класса Hero
# Методы:
# start(): начинает игру, чередует ходы игрока и компьютера, пока один из героев не умрет. Выводит информацию о каждом ходе
# (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.

import random

class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, power, other):
        effect = random.randint(0, 10)
        other.health -= int((power * effect/10) // 1)
        print(f"Противник применил защитный прием. Сила удара получилась {int((power * effect/10) // 1)}")
        if self.attack_power > 10:
            self.attack_power -= int((effect / 5) // 1)

    def is_alive(self):
        return self.health


class Game():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Бой начинается")

        while True:
            if self.computer.health <= 0:
                print("Player победил!!!!!!!")
                break
            elif self.player.health <= 0:
                print("Computer победил. Не расстраивайтесь. Следующий раз повезет.")
                break

            power = int(input(f"Ваша максимальная сила удара: {self.player.attack_power}. С какой силой будете бить? "))
            print(f"Player нанес удар силой {power}")
            self.player.attack(power, self.computer)
            print(f"У Computer осталось {self.computer.health} жизней")

            power = random.randint(1, self.computer.attack_power)
            print(f"Computer нанес удар силой {power}")
            self.computer.attack(power, self.player)
            print(f"У Player осталось {self.player.health} жизней")


player = Hero("Player")
computer = Hero("Computer")

game = Game(player, computer)
game.start()




