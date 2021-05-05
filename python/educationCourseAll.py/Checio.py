# ЗАДАЧА 1. Multiply (Intro)
#
# Итак, это самая простая миссия. Напишите функцию, которая будет получать
# 2 числа и возвращать результат произведения этих чисел.
#
# Входные данные: Два аргумента. Оба int
# Выходные данные: Int.
#
# Пример:
# mult_two(2, 3) == 6
# mult_two(1, 0) == 0

def mult_two(a: int, b:int) -> int:
    return a*b


# ЗАДАЧА 2. First Word (simplified)
#
# Дана строка и нужно найти ее первое слово.
# Это упрощенная версия миссии First Word, которую можно решить позднее.
# Строка состоит только из английских символов и пробелов.
# В начале и в конце строки пробелов нет.
#
# Входные данные: строка.
# Выходные данные: строка.
#
# Пример:
# first_word("Hello world") == "Hello"
# 1
# Как это используется: Первое слово — это команда в командной строке.
# Предусловия: Текст может содержать буквы a-z, A-Z и пробелы.

def first_word(text: str) -> str:

    return text.split()[0]


# ЗАДАЧА 3. Acceptable Password I
#
# Вы начали серию задач связаную с паролями. Каждая следующая задача связана с предыдущей.
# Каждая следующая задача будет сложнее предыдущей.
# В этой задаче, Вам нужно создать функцию проверки пароля.
#
# Условия проверки:
# длина пароля должна быть больше 6.
#
# Входные данные: Строка.
# Выходные данные: Логический тип.
#
# Пример:
# is_acceptable_password('short') == False
# is_acceptable_password('muchlonger') == True
# 1
# 2
# Для чего это нужно: Для проверки заполнения пароля. Кроме того, полезно будет научиться оценивать задачи.

def is_acceptable_password(password: str) -> bool:
    if len(password) > 6:
        return True
    else:
        return False

# Решение через lambda
is_acceptable_password_lambda = lambda password: len(password) > 6


# ЗАДАЧА 4. Number Length
#
# Вам дано положительное целое число. Определите сколько цифр оно имеет.
#
# Входные данные: Положительное целое число
# Выходные данные: Целое число.
#
# Пример:
# number_length(10) == 2
# number_length(0) == 1

def number_length(a: int) -> int:
    result = len(str(a))
    return result


# ЗАДАЧА 5. End Zeros
#
# Попробуйте выяснить какое количество нулей содержит данное число в конце.
#
# Входные данные: Положительное целое число (int).
# Выходные данные: Целое число (int).
#
# Пример:
# end_zeros(0) == 1
# end_zeros(1) == 0
# end_zeros(10) == 1
# end_zeros(101) == 0

def end_zeros(num: int) -> int:
    num_str=str(num)
    num_str=num_str[::-1]
    count=0

    for i in num_str:
        if i=='0':
            count+=1
        else:
            break
    return count
#--------------------
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))
#--------------------
end_zeros = lambda num: len(str(num)) - len(str(num).rstrip('0'))
#--------------------
import re
def end_zeros(num: int) -> int:
    return len(re.search('0*$', str(num)).group())
#--------------------
def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))

def end_zeros(number):
    number = str(number)
    if number[-1:] != '0':
        return 0
    return 1 + end_zeros(number[:-1])

def end_zeros(number):
    if not number:
       return 1
    if not number % 10:
       return 1 + end_zeros(number // 10)
    return 0

def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result

def end_zeros(number):
    en = enumerate(str(number)[::-1])
    return not number or next(i for i, x in en if x != '0')

def end_zeros(number):
    from itertools import takewhile
    number = str(number)[::-1]
    return len(list(takewhile(lambda x: x == '0', number)))

# ЗАДАЧА 6. Backward String
#
# Верните данную строку в перевернутом виде.
#
# Входные данные: Строка.
# Выходные данные: Строка.
#
# Пример:
# backward_string('val') == 'lav'
# backward_string('') == ''
# backward_string('ohho') == 'ohho'
# backward_string('123456789') == '987654321'

def backward_string(val: str) -> str:
    string = "".join(reversed(val))
    return string
#--------------------
backward_string = lambda val: val[::-1]
#--------------------
def backward_string(val: str) -> str:
    return val[::-1]
#--------------------

# ЗАДАЧА 7. Remove All Before
#
# Не все элементы важны. Вам нужно удалить из список все элементы до указаного.
# На примере мы имеем список [1, 2, 3, 4, 5] где нужно было удалить все элементы до 3 - 1 и 2 соответственно.
# Есть два ньюанса: (1) если в списке нет элемента до которого нужно удалить остальные элементы, то список не должен измениться. (2) если list пустой, то он должен остаться пустым.
#
# Входные данные: Список и элемент до которого нужно удалить другие элементы.
# Выходные данные: Набор значений (кортеж, список, итератор ...).
#
# Пример:
# remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
# remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]

from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    return items[items.index(border):] if border in items else items

from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        del items[:items.index(border)]
    return items

def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items

from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    if list == [] or border not in items:
        return items
    else:
        x = items.index(border)
        return items[x:]


    # ЗАДАЧА 8
#
#
# ЗАДАЧА 9
#
#
#
# ЗАДАЧА 10
#
# ЗАДАЧА 11
#
#
#
# ЗАДАЧА 12
#
# ЗАДАЧА 13
#
#
#
# ЗАДАЧА 14
#
#