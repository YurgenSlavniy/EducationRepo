# Практическое задание
# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»
# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.
# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.
# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

# 1 .#
def anketa():
    name = input('Введите имя')
    age = int(input('Введите возраст'))
    town = input('Введите город проживания')
    print(name, age, 'год (а), проживает в городе ', town )

anketa()

# 2 .
def max_from_3(first, second, third):
    numbers = [first, second, third]
    print(max(numbers))

max_from_3(90, 4, 28)

# 3 .
playername = input('Введите имя игрока: ')
player = {'name': playername, 'health': 100, 'damage': 75}
enemy = {'health': 74, 'damage': 34}


def attack(person1, person2):
    person1 = player
    person2 = enemy
    fight = person2['health'] - person1['damage']
    if fight > 0:
        person2['health'] = fight
        print(person2)
    else:
        print('Враг Повержен!')


attack(player, enemy)

# 4.

player['armor'] = 1.2
enemy['armor'] = 1.5

def arm_atack(person1, person2):
    person1 = player
    person2 = enemy
    uron = person1['damage']/person1['armor']
