#-----------------#
# Elementary:     #
#-----------------#

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

def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))

end_zeros = lambda num: len(str(num)) - len(str(num).rstrip('0'))

import re
def end_zeros(num: int) -> int:
    return len(re.search('0*$', str(num)).group())

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

backward_string = lambda val: val[::-1]

def backward_string(val: str) -> str:
    return val[::-1]


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

# ЗАДАЧА 8. All Upper I
#
# Проверить все ли символы в строке являются заглавными.
# Если строка пустая или в ней нет букв - функция должна вернуть True.
#
# Входные данные: Строка.
# Выходные данные: Логический тип.
#
# Пример:
# is_all_upper('ALL UPPER') == True
# is_all_upper('all lower') == False
# is_all_upper('mixed UPPER and lower') == False
# is_all_upper('') == True
# is_all_upper('444') == True
# is_all_upper('55 55 5') == True
# Условия: a-z, A-Z, 1-9 и пробелы

def is_all_upper(text: str) -> bool:
    return text == text.upper()

import re
def is_all_upper(text: str) -> bool:
    return len(re.sub(r'[a-z]', '', text))==len(text)

def is_all_upper(text: str) -> bool:
    text=text.replace(" ","")
    if text.isupper()==True:
        return True
    elif len(text)==0:
        return True
    elif text.isdigit()==True:
        return True
    elif text.isspace()==True:
        return True
    else:
        return False


def is_all_upper(text: str) -> bool:
    result = True
    if not text.strip() or text.isupper() or any(char.isdigit() for char in text):
        result = True
    elif text.islower() or (not text.islower() and not text.isupper()):
        result = False
    return result


# ЗАДАЧА 9. Replace First
#
# В данном списке первый элемент должен стать последним.
# Пустой список или список из одного элемента не должен измениться.
#
# Входные данные: Список.
# Выходные данные: Набор элементов.
#
# Пример:
# replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# replace_first([1]) == [1]

from typing import Iterable
def replace_first(items: list) -> Iterable:
    if items == []:
        return items
    else:
        a = items[0]
        del items[0]
        items.append(a)
        return items

# Change items IN-PLACE.
def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items

# Slices
def replace_first(items: list) -> list:
    return items[1:] + items[:1]

# collections.deque have an useful method: rotate.
from collections import deque
def replace_first(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items

replace_first = lambda a: a[1:] + a[:1]

from typing import Iterable
def replace_first(items: list) -> Iterable:
    return items[1:] + items[:1]

from typing import Iterable
def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        items.append(items.pop(0))
    return items


# ЗАДАЧА 10. Max Digit
#
# У вас есть число и нужно определить
# какая цифра из этого числа является наибольшей.
#
# Входные данные: Положительное целое число.
# Выходные данные: Целое число (0-9).
#
# Пример:
# max_digit(0) == 0
# max_digit(52) == 5
# max_digit(634) == 6
# max_digit(1) == 1
# max_digit(10000) == 1

def max_digit(number: int) -> int:
    return int(max(i for i in str(number)))

def max_digit(number):
    number = set(str(number))
    return int(max(number))

def max_digit(number: int) -> int:
    text = str(number)
    for n in range(9, -1, -1):
        if str(n) in text:
            return n

max_digit = lambda number: int(max(str(number)))


# ЗАДАЧА 11. Split Pairs
#
# Разделите строку на пары из двух символов.
# Если строка содержит нечетное количество символов,
# пропущенный второй символ последней пары должен быть заменен подчеркиванием ('_').
#
# Входные данные: Строка.
# Выходные данные: Массив строк.
#
# Пример:
# split_pairs('abcd') == ['ab', 'cd']
# split_pairs('abc') == ['ab', 'c_']
# Предварительное условие: 0<=len(str)<=100

def split_pairs(a):
    if len(a) == 0:
        a = a
    elif len(a) % 2 == 0:
        a = a
    else:
        a = a + '_'
    n = 2
    chunks = [a[i:i+n] for i in range(0, len(a), n)]
    return chunks

def split_pairs(a):
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]

from textwrap import wrap
def split_pairs(a):
    a = a + '_' if len(a) % 2 else a
    return wrap(a, 2)

import itertools, operator
def split_pairs(a):
    it = itertools.chain(a, '_')
    return map(operator.add, it, it)

def split_pairs(s):
    N = len(s)
    if N % 2 == 1: s += "_"
    return [s[i:i+2] for i in range(0,N,2)]

# ЗАДАЧА 12
#
# ЗАДАЧА 13
#
#
#
# ЗАДАЧА 14
#
#