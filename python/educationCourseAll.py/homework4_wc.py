## Практическое задание
# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def person_info(name, age, city):
    result = f'{name}, {age}, год(а) проживает в городе {city}'
    return result
print(person_info('Василий', 21, 'Москва'))

# мы должны вспомнить об основных атрибутах функции
# это её параметры (name, age, city), название person_info
# и возвращаемое значение return result.
#
# Объявляем функцию def person_info, у неё три параметра (name, age, city)
# создаём переменную result, она будет строкой и формируем строку удобным нам образом
# f'{name}, {age}, год(а) проживает в городе {city}'
# подставляем в строку параметры функции
# после того как готов результат,делаем ретёрн и  будем его возвращать
# после того как функция написана мы её вызываем и передаём параметры .начинаем пользоваться
# print(person_info('Василий', 21, 'Москва'))

# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def get_max(a, b, c):
    result = max([a, b, c])
    return result
result = get_max(4, 7, 12)
print(result)
# Объявляем функцию def get_max
# у неё три параметра (a, b, c) три числа
# result = max([a, b, c]) - сформируем список из этих чисел
# и далее применим к нему функцию max
# не забываем делать return - возвращать результат работы функции
# теперь можно функцию использовать, например объявляем переменную result =
# вызываем функцию result = get_max()
# подставляем переменные: result = get_max(4, 7, 12)
# print(result) проверяем как работает, выводим результат

# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. ### Поэкспериментируйте с значениями урона и жизней по желанию.
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои.
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого.
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого.
# Функция должна сама работать со словарями и изменять их значения.

player_name = input('Введите имя игрока: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50
}

enemy_name = ('Введите имя врага: ')
enemy = {
    'name': enemy_name,
    'health': 50,
    'damage': 30
}

def attack(unit, target):
    target['health'] -= unit['damage']

attack(player, enemy)
print(player, enemy)

attack(enemy, player)
print(player, enemy)

# Создадим 2 словаря для описания сущностей.
# Словари содержат ключи: имя, здоровье, урон
# имя вводит пользователь
# def attack - создаём функцию, придумываем названия параметров:
# первый параметр - unit - кто атакует
# второй параметр - target - цель , кого атакуют
# т.к. имеем дело со словарями, будем их менять.
# берём словарь и ключ target['health'] и из этого здоровья вычитаем значение другого ключа
# target['health'] -= unit['damage']
# проверяем как работает
# attack(player, enemy) и attack(enemy, player)
# вызываем функцию с разными параметрами

# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
#
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа.

player_name = input('Введите имя игрока: ')
player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}

enemy_name = ('Введите имя врага: ')
enemy = {
    'name': enemy_name,
    'health': 50,
    'damage': 30,
    'armor': 1.5
}
def get_demage(damage, armor):
    return damage/armor
def attack(unit, target):
    damage = get_demage(unit['damage'], target['armor'])
    target['health'] -= damage

attack(player, enemy)
print(player, enemy)

attack(enemy, player)
print(player, enemy)

# сначала добавим в словари новые значения  'armor': 1.2
# напишем ещё одну функцию get_demage. в неё передаём 2 параметра
# damage - урон и armor - величина брони
# эта функция будет возвращать результат return damage/armor
# теперь мы можем ф-ю get_demage использовать в функции attack
# для того чтобы расчитать величину урона
# damage = get_demage(unit['damage'], target['armor'])
# теперь  damage = get_demage
# в параметры нам надо передать сначала урон. Урон наносит unit
# берём unit['damage']
# второй параметр - это броня
# броню мы берём у target
# target['armor']
# после того как вычислили урон, отнимаем его от здоровья
# target['health'] -= damage