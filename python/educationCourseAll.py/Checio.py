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
#...........................................................

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
#...........................................................

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
#-----------------------------------------------------------
# Решение через lambda
is_acceptable_password_lambda = lambda password: len(password) > 6
#...........................................................

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
#...........................................................

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
#-----------------------------------------------------------
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))
#-----------------------------------------------------------
end_zeros = lambda num: len(str(num)) - len(str(num).rstrip('0'))
#-----------------------------------------------------------
import re
def end_zeros(num: int) -> int:
    return len(re.search('0*$', str(num)).group())
#-----------------------------------------------------------
def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))
#-----------------------------------------------------------
def end_zeros(number):
    number = str(number)
    if number[-1:] != '0':
        return 0
    return 1 + end_zeros(number[:-1])
#-----------------------------------------------------------
def end_zeros(number):
    if not number:
       return 1
    if not number % 10:
       return 1 + end_zeros(number // 10)
    return 0
#-----------------------------------------------------------
def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result
#-----------------------------------------------------------
def end_zeros(number):
    en = enumerate(str(number)[::-1])
    return not number or next(i for i, x in en if x != '0')
#-----------------------------------------------------------
def end_zeros(number):
    from itertools import takewhile
    number = str(number)[::-1]
    return len(list(takewhile(lambda x: x == '0', number)))
#...........................................................

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
#-----------------------------------------------------------
backward_string = lambda val: val[::-1]
#-----------------------------------------------------------
def backward_string(val: str) -> str:
    return val[::-1]
#...........................................................

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
#-----------------------------------------------------------
from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    if border in items:
        del items[:items.index(border)]
    return items
#-----------------------------------------------------------
def remove_all_before(items, border):
    try:
        return items[items.index(border):]
    except ValueError:
        return items
#-----------------------------------------------------------
from typing import Iterable
def remove_all_before(items: list, border: int) -> Iterable:
    if list == [] or border not in items:
        return items
    else:
        x = items.index(border)
        return items[x:]
#...........................................................

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
#-----------------------------------------------------------
import re
def is_all_upper(text: str) -> bool:
    return len(re.sub(r'[a-z]', '', text))==len(text)
#-----------------------------------------------------------
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
#-----------------------------------------------------------
def is_all_upper(text: str) -> bool:
    result = True
    if not text.strip() or text.isupper() or any(char.isdigit() for char in text):
        result = True
    elif text.islower() or (not text.islower() and not text.isupper()):
        result = False
    return result
#...........................................................

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
#-----------------------------------------------------------
# Change items IN-PLACE.
def replace_first(items: list) -> list:
    if items:
        items.append(items.pop(0))
    return items
#-----------------------------------------------------------
# Slices
def replace_first(items: list) -> list:
    return items[1:] + items[:1]
#-----------------------------------------------------------
# collections.deque have an useful method: rotate.
from collections import deque
def replace_first(items: list) -> deque:
    items = deque(items)
    items.rotate(-1)
    return items
#-----------------------------------------------------------
replace_first = lambda a: a[1:] + a[:1]
#-----------------------------------------------------------
from typing import Iterable
def replace_first(items: list) -> Iterable:
    return items[1:] + items[:1]
#-----------------------------------------------------------
from typing import Iterable
def replace_first(items: list) -> Iterable:
    if len(items) > 1:
        items.append(items.pop(0))
    return items
#...........................................................

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
#-----------------------------------------------------------
def max_digit(number):
    number = set(str(number))
    return int(max(number))
#-----------------------------------------------------------
def max_digit(number: int) -> int:
    text = str(number)
    for n in range(9, -1, -1):
        if str(n) in text:
            return n
#-----------------------------------------------------------
max_digit = lambda number: int(max(str(number)))
#...........................................................

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
#-----------------------------------------------------------
def split_pairs(a):
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]
#-----------------------------------------------------------
from textwrap import wrap
def split_pairs(a):
    a = a + '_' if len(a) % 2 else a
    return wrap(a, 2)
#-----------------------------------------------------------
import itertools, operator
def split_pairs(a):
    it = itertools.chain(a, '_')
    return map(operator.add, it, it)
#-----------------------------------------------------------
def split_pairs(s):
    N = len(s)
    if N % 2 == 1: s += "_"
    return [s[i:i+2] for i in range(0,N,2)]
#...........................................................

# ЗАДАЧА 12. Beginning Zeros
#
# Вам дана строка состоящая только из цифр.
# Вам нужно посчитать сколько нулей ("0")
# находится в начале строки.
#
# Входные данные: Строка, состоящая только из цифр.
# Выходные данные: Целое число.
#
# Пример:
# beginning_zeros('100') == 0
# beginning_zeros('001') == 2
# beginning_zeros('100100') == 0
# beginning_zeros('001001') == 2
# beginning_zeros('012345679') == 1
# beginning_zeros('0000') == 4
# Строка может иметь цифры: 0-9

def beginning_zeros(number: str) -> int:
    result = 0
    for n in number:
        if int(n) == 0:
            result += 1
        else:
            return result
    return result
#-----------------------------------------------------------
beginning_zeros = lambda number: len(number) - len(number.lstrip('0'))
#-----------------------------------------------------------
from itertools import takewhile
beginning_zeros = lambda number: len(list(takewhile(lambda x: x=='0', number)))
#-----------------------------------------------------------
def beginning_zeros(number: str) -> int:
    return (len(number)-len(number.lstrip("0")))
#-----------------------------------------------------------
def beginning_zeros(number: str) -> int:
    zero = 0
    for num in number:
        if num != '0':
            break
        else:
            zero += 1
    return zero
#-----------------------------------------------------------
import re
def beginning_zeros(number: str) -> int:
    return len(re.sub(r'[^0].*$', '', number))
#...........................................................

# ЗАДАЧА 13. Nearest Value
#
# Найдите ближайшее значение к переданному.
# Вам даны список значений в виде множества (Set) и значение,
# относительно которого, надо найти ближайшее.
#
# Например, мы имеем следующий ряд чисел: 4, 7, 10, 11, 12, 17.
# И нам нужно найти ближайшее значение к цифре 9.
# Если отсортировать этот ряд по возрастанию,
# то слева от 9 будет 7, а справа 10.
# Но 10 - находится ближе, чем 7,
# значит правильный ответ 10.
#
# Несколько уточнений:
#
# Если 2 числа находятся на одинаковом расстоянии - необходимо выбрать наименьшее из них;
# Ряд чисел всегда не пустой, т.е. размер >= 1;
# Переданное значение может быть в этом ряде, а значит оно и является ответом;
# В ряде могут быть как положительные, так и отрицательные числа, но они всегда целые;
# Ряд не отсортирован и состоит из уникальных чисел.
#
# Входные данные: Два аргумента. Ряд значений в виде set. Искомое значение - int
# Выходные данные: Int.
#
# Пример:
# nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
# nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7

def nearest_value(values, one):
    return min({(abs(n-one), n) for n in values})[1]
#-----------------------------------------------------------
def nearest_value(values: set, one: int) -> int:
    return sorted(sorted(values), key=lambda x: abs(one - x))[0]
#-----------------------------------------------------------
def nearest_value(values: set, one: int) -> int:
    lista = sorted(values)
    for element in lista:
        diff = abs(one - element)
        try:
            if diff < prevDiff:
                prevDiff = diff
                nearest = element
        except UnboundLocalError:
            prevDiff = diff
            nearest = element
    return nearest
#-----------------------------------------------------------
def nearest_value(values: set, one: int) -> int:
    l = list(values);
    l.sort(key=lambda x:(abs(x - one),x));
    return l[0];
#-----------------------------------------------------------
def nearest_value(values: set, one: int) -> int:
    values = list(values)
    if one in values:
        return one
    else:
        values.append(one)
        values.sort()
        ind = values.index(one)
        if ind == 0:
            return values[1]
        elif ind == len(values) - 1:
            return values[-2]
        else:
            prev = values[ind - 1]
            next = values[ind + 1]
            d_prev = one - prev
            d_next = next - one
            if d_next == d_prev:
                return prev
            elif d_prev < d_next:
                return prev
            else:
                return next
#-----------------------------------------------------------
def nearest_value(values: set, one: int) -> int:
    def distance(value): return abs(value - one), value > one
    return min(values, key=distance)
#-----------------------------------------------------------
def nearest_value(values: set, one: int) -> int:
    return sorted([(abs(v - one), v) for v in values], key = lambda item: (item[0], item[1]))[0][1]
#...........................................................

# ЗАДАЧА 14. Between Markers (simplified)
#
# Вам дана строка и два маркера (начальный и конечный).
# Вам необходимо найти текст, заключенный между двумя этими маркерами.
# Но есть несколько важных условий:
#
# Начальный и конечный маркеры всегда разные.
# Начальный и конечный маркеры всегда размером в один символ.
# Начальный и конечный маркеры всегда есть в строке и идут один за другим.
#
# Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.
# Output: Строка.
#
# Пример:
# between_markers('What is >apple<', '>', '<') == 'apple'
# Как это используется: Может использоваться для парсинга небольшой верстки.
#
# Предусловия: Не может быть более одного маркера одного типа.

def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin) + 1:text.find(end)]
#-----------------------------------------------------------
def between_markers(text: str, begin: str, end: str) -> str:
    text = text.split(begin)[1]
    return text.split(end)[0]
#-----------------------------------------------------------
def between_markers(text, m1, m2):
    return text[text.index(m1)+1:text.index(m2)]
#-----------------------------------------------------------
from re import finditer
def between_markers(text, *m):
    return next(finditer((r"%s(.*)%s" % m).replace('[', '\[').replace(']', '\]'), text)).groups()[0]
#-----------------------------------------------------------
def between_markers(text: str, begin: str, end: str) -> str:
    b = text.find(begin)
    e = text.find(end)
    return text[b + 1:e]
#...........................................................

# ЗАДАЧА 15. Correct Sentence
#
# На вход Вашей функции будет передано одно предложение.
# Необходимо вернуть его исправленную копию так,
# чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
#
# Обратите внимание на то, что не все исправления необходимы.
# Если предложение уже заканчивается на точку,
# то добавлять еще одну не нужно, это будет ошибкой
#
# Входные аргументы: Строка (A string).
# Выходные аргументы: Строка (A string).
#
# Пример:
# correct_sentence("greetings, friends") == "Greetings, friends."
# correct_sentence("Greetings, friends") == "Greetings, friends."
# correct_sentence("Greetings, friends.") == "Greetings, friends."
# Предусловия: В начале и конце нет пробелов, текст состоит только из пробелов, a-z A-Z , и .

def correct_sentence(str):
    text = ""
    str = list(str)
    str[0] = str[0].upper()
    if "." not in str:
        str += "."
    str = "".join(str)
    return str
#-----------------------------------------------------------
def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if text[-1] != '.':
        text = text + '.'
    return text
#-----------------------------------------------------------
def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if text[-1] != ".":
        text +='.'
    return text
#-----------------------------------------------------------
def correct_sentence(text: str) -> str:
    if text[-1] == '.':
        return text[0].upper() + text[1:]
    else:
        return text[0].upper() + text[1:] + '.'
#-----------------------------------------------------------
def correct_sentence(text: str) -> str:
    text = list(text)
    begin = text[0]
    end = text[-1]
    text[0] = begin if begin.isupper() else begin.upper()
    text = text if end == '.' else text + ['.']
    return ''.join(text)
#-----------------------------------------------------------
def correct_sentence(text: str) -> str:
    return text[0].capitalize() + text.rstrip('.')[1:] + '.'
#-----------------------------------------------------------
def correct_sentence(text: str) -> str:
    return text[0].upper() + text[1:] + '.' * (not text.endswith('.'))
#-----------------------------------------------------------
def correct_sentence(text: str) -> str:
    a='' if text[-1]=='.' else '.'
    return text[0].upper()+ text[1:] +a
#...........................................................

# ЗАДАЧА 16. Is Even
#
# Проверить является ли число четным или нет.
# Ваша функция должна возвращать True если число четное,
# и False если число не четное.
#
# Входные данные: Целое число.
# Выходные данные: Логический тип.
#
# Пример:
# is_even(2) == True
# is_even(5) == False
# is_even(0) == True
# Где это используется: (математика используется везде)
# Условия: целые числа даны в диапазоне от -1000 и до 1000

def is_even(num: int) -> bool:
    if num % 2 == 0:
        return True
    elif num == 0:
        return True
    else:
        return False
#-----------------------------------------------------------
def is_even(num: int) -> bool:
    return num & 1 == 0
#-----------------------------------------------------------
def is_even(num: int) -> bool:
    return not bool(num%2)
#-----------------------------------------------------------
def is_even(num: int) -> bool:
    return not num % 2
#-----------------------------------------------------------
def is_even(num: int) -> bool:
    if num % 2 != 1:
        return True
    return False
#-----------------------------------------------------------
def is_even(num: int) -> bool:
    return bin(num)[-1]=='0'

# -----------------------------------
#   END ELEMENTARY 16/16
# -----------------------------------

# -----------------------------------
#   START HOME 0/20
# -----------------------------------


# ЗАДАЧА 1. Sum Numbers
#
# Вам дан текст в котором нужно просуммировать числа,
# но только разделенные пробелом.
# Если число является частью слова, то его суммировать не нужно.
#
# Текст состоит из чисел, пробелом и английского алфавита.
#
# Входные данные: Строка.
# Выходные данные: Целое число.
#
# Пример:
# sum_numbers('hi') == 0
# sum_numbers('who is 1st here') == 0
# sum_numbers('my numbers is 2') == 2
# sum_numbers('This picture is an oil on canvas '
#  'painting by Danish artist Anna '
#  'Petersen between 1845 and 1910 year') == 3755
# sum_numbers('5 plus 6 is') == 11
# sum_numbers('') == 0

def sum_numbers(text: str) -> int:
    return sum(( int(word) for word in text.split() if word.isdigit()))
#-----------------------------------------------------------
def sum_numbers(text: str) -> int:
    s = 0
    for l in text.split():
        try:
            s += int(l)
        except ValueError:
            continue
    return s
#-----------------------------------------------------------
class text_with_number:
    def __init__(self, text):
        self.text = text
    def add_numbers(self):
        answer = 0
        for word in self.text.split():
            if word.isdigit():
                answer += int(word)
        return answer
def sum_numbers(text):
    return text_with_number(text).add_numbers()
#-----------------------------------------------------------
def sum_numbers(text: str) -> int:
    count = 0
    spl_text = text.split(' ')
    for i in spl_text:
        i.replace(' ', '')
        if i.isnumeric():
            count += int(i)
    return count
#-----------------------------------------------------------
def sum_numbers(text: str) -> int:
    # your code here
    return sum(map(lambda x: int(x), filter(lambda x: x.isnumeric(), text.split())))
#-----------------------------------------------------------
def sum_numbers(text: str) -> int:
    summary = 0
    lsttext = text.split()
    for countwords in range(0, len(lsttext)):
        if lsttext[countwords].isdigit(): summary += int(lsttext[countwords])
    return summary
#-----------------------------------------------------------
def sum_numbers(text: str) -> int:
    L = text.split()
    ans = 0
    for n in L:
        if n.isdecimal():
            ans += int(n)
    return ans
#-----------------------------------------------------------
def sum_numbers(text: str) -> int:
    # your code here
    def numbers(t):
        try:
            return int(t)
        except:
            return 0
    try:
        return __import__("functools").reduce(lambda a,c: a+c,(numbers(t) for t in text.split()))
    except:
        return 0
#...........................................................

# ЗАДАЧА 2. Even the Last
#
# Дан массив целых чисел.
# Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд),
# затем перемножить эту сумму и последний элемент исходного массива.
# Не забудьте, что первый элемент массива имеет индекс 0.
#
# Для пустого массива результат всегда 0 (ноль).
#
# Входные данные: Список (list) целых чисел (int).
# Выходные данные: Число как целочисленное (int).
#
# Примеры:
# checkio([0, 1, 2, 3, 4, 5]) == 30
# checkio([1, 3, 5]) == 30
# checkio([6]) == 36
# checkio([]) == 0
# 1
# 2
# 3
# 4
# Зачем это нужно: Индексы и срезы - очень важные элементы программирования,
# как на Python, так и на других языках. Это поможет вам в дальнейшем.
#
# Предусловия: 0 ≤ len(array) ≤ 20
# all(isinstance(x, int) for x in array)
# all(-100 < x < 100 for x in array)

def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    return sum(array[i] for i in range(len(array)) if i % 2 == 0) * array[-1] if len(array) > 0 else 0
#-----------------------------------------------------------
def checkio(array):
    if len(array) == 0:
        return 0
    return sum(array[0::2]) * array[-1]
#-----------------------------------------------------------
checkio=lambda x: sum(x[::2])*x[-1] if x else 0
#-----------------------------------------------------------
def checkio(array):
    return 0 if not array else sum(array[::2]) * array[-1]
#-----------------------------------------------------------
from itertools import islice
def checkio(array):
    return sum(islice(array, None, None, 2)) * array[-1] if array else 0
#-----------------------------------------------------------
def checkio(array):
#    from numpy import sum
    if len(array) > 0:
        return int(sum(array[::2])*array[-1])
    else:
        return 0
#-----------------------------------------------------------
# import numpy as np

class even_the_last:
    def __init__(self, array):
#        array = np.array(array)
        self.array = array

    def perform(self):
        if not self.array.shape[0]:
            return 0
#        even_sum = np.sum(self.array[0::2])
        last = self.array[-1]
#        return even_sum * last

def checkio(array):
    return even_the_last(array).perform()
#-----------------------------------------------------------
def checkio(array: list) -> int:
    """
        sums even-indexes elements and multiply at the last
    """
    sum = 0
    if len(array) == 0:
        return 0
    else:
        for n in range(len(array)):
            if (n % 2) == 0:
                sum = sum + array[n]
            result = sum * array[-1]
        return result
#...........................................................

# ЗАДАЧА 3. Three Words
#
# Давайте научим наших роботов отличать слова от чисел.
# Дана строка со словами и числами, разделенными пробелами
# (один пробел между словами и/или числами).
# Слова состоят только из букв.
# Вам нужно проверить есть ли в исходной строке три слова подряд .
# Для примера,
# в строке "start 5 one two three 7 end"
# есть три слова подряд.
#
# Входные данные: Строка со словами (str).
# Выходные данные: Ответ как логическое выражение (bool), True или False.
#
# Примеры:
# checkio("Hello World hello") == True
# checkio("He is 123 man") == False
# checkio("1 2 3 4") == False
# checkio("bla bla bla bla") == True
# checkio("Hi") == False
# 1
# 2
# 3
# 4
# 5
# Зачем это нужно: Эта задача подскажет вам как работать со строками и покажет некоторые полезные функции.
#
# Предусловия: Исходная строка содержит только слова и/или числа.
# Смешанных слов нет (перемешанные цифры и буквы).
# 0 < len(words) < 100

def checkio(words: str) -> bool:
    count = 0
    for i in words.split():
        if not i.isalpha():
            count = 0
        else:
            count += 1
        if count == 3:
            return True
    return False
#-----------------------------------------------------------
def checkio(words: str) -> bool:
    count = 0
    word_list = list(words.split())
    for word in word_list:
        count = (count + 1) * word.isalpha()
        if count == 3:
            return True
    else:
        return False
#-----------------------------------------------------------
def checkio(words: str):
    wl=words.split(' ')
    tf=list(map(lambda x: bool(x.isalpha()),wl))
    tf=''.join(str(tf))
    return bool('True, True, True' in tf)
#-----------------------------------------------------------
# import numpy as np
#
# class Three_Words:
#     def __init__(self, words):
#         self.words = words
#
#     def perform(self):
#       foo = np.array([w for w in self.words.split()])
#         count = 0
#        for i in range(np.size(foo)):
#           if not foo[i].isdigit():
#                 count += 1
#                 if count == 3:
#                     return True
#             else:
#                 count = 0
#
#         return False
#-----------------------------------------------------------
def checkio(words: str) -> bool:
    successive_words = 0

    for word in words.split():
        successive_words = (successive_words + 1 if word.isalpha() else 0)
        if successive_words == 3:
            return True

    return False
#-----------------------------------------------------------
from itertools import groupby


def checkio(words: str) -> bool:
    words = map(str.isalpha, words.split())
    return max(sum(j) for _, j in groupby(words)) >= 3
#...........................................................

# ЗАДАЧА 4. Right to Left
#
# "На протяжении веков, левши страдали от дискриминации в мире,
# созданном для правшей."
# Santrock, John W. (2008).
# Motor, Sensory, and Perceptual Development.
#
# "Большинство людей (70-95%) правши,
# меньшинство (5-30 %) левши,
# и неопределеное число людей
# вероятно лучше всего охарактеризовать,
# как "симметричные"."
# Scientific American.
# www.scientificamerican.com
#
# Один робот был занят простой задачей:
# объединить последовательность строк
# в одно выражение для создания инструкции
# по обходу корабля.
# Но робот был левша и зачастую шутил и запутывал своих друзей правшей.
#
# Дана последовательность строк.
# Вы должны объединить эти строки в блок текста,
# разделив изначальные строки запятыми.
# В качестве шутки над праворукими роботами,
# вы должны заменить все вхождения слова
# "right" на слова "left",
# даже если это часть другого слова.
# Все строки даны в нижнем регистре.
#
# Входные данные: Последовательность строк.
# Выходные данные: Текст, как строка.
#
# Пример:
#
# left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# left_join(("bright aright", "ok")) == "bleft aleft,ok"
# left_join(("brightness wright",)) == "bleftness wleft"
# left_join(("enough", "jokes")) == "enough,jokes"


# Как это используется: Это просто пример операций,
# использующих строки и последовательности.
#
# Предусловие:
# 0 < len(phrases) < 42

message_text = ("left", "right", "left", "stop")
print(type(message_text))
def left_change_right(message_text):
    jointext = ','.join(message_text)
    print(jointext)
    print(type(jointext))
    jointext = jointext.replace('left', 'right')
    return jointext
#-----------------------------------------------------------
def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    strphrases = ','.join(phrases)
    newstrphrases = strphrases.replace('right', 'left')
    return newstrphrases
#-----------------------------------------------------------
def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    return (",".join(phrases)).replace("right","left")
#-----------------------------------------------------------
def left_join(phrases: tuple) -> str:
    """
        Join strings and replace "right" to "left"
    """
    phrases_string = ','.join(list(phrases))
    return phrases_string.replace('right', 'left')
#-----------------------------------------------------------
def left_join(phrases: tuple, /) -> str:
    """
        Join strings and replace "right" to "left"
    """

    phrases = ",".join(list(phrases)).replace("right", "left")

    return phrases
#-----------------------------------------------------------
# import numpy as np

class right_to_left():
    def __init__(self, phrases):
        self.phrases = phrases

#    def perform(self):
#        replaced_words_array = np.array([p.replace('right', 'left') for p in self.phrases])
#        replaced_words_list = replaced_words_array.tolist()
#        return ",".join(replaced_words_list)

def left_join(phrases: tuple) -> str:
    foo = right_to_left(phrases)
    return foo.perform()

def left_join(phrases):
    return ",".join(k.replace('right', 'left') for k in phrases)
#-----------------------------------------------------------
# # coding: utf-8
# 左 = 'left'
# 右 = 'right'
# 点 = ','
# 置換 = str.replace
# 合併 = str.join
#
# left_join = lambda 文:置換(合併(点, 文), 右, 左)
#-----------------------------------------------------------
def left_join(phrases):
    """
        Join strings and replace "right" to "left"
    """
    a=""
    for i in phrases:
        a=a+","+i
    a=a[1:].replace("right", "left")
    return a
#...........................................................

# ЗАДАЧА 5. First Word
#
# Дана строка и нужно найти ее первое слово.
# При решении задачи обратите внимание на следующие моменты:
# - В строке могут встречатся точки и запятые
# - Строка может начинаться с буквы или, к примеру, с пробела или точки
# - В слове может быть апостроф и он является частью слова
# - Весь текст может быть представлен только одним словом и все

# Входные параметры: Строка.
# Выходные параметры: Строка.
#
# Пример:
# first_word("Hello world") == "Hello"
# first_word("greetings, friends") == "greetings"

# How it is used: first word is a command in command line
# Precondition: text can contain a-z A-Z , . '

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    return text.replace('.', ' ').replace(',', ' ').split()[0]
#-----------------------------------------------------------

# Explanation
# findall returns a list of all the matches so we need to append [0] to return only the first
# \b matches a word boundary
# [\w'] matches any word character or '
# [\w']+ is a greedy match for an uninterrupted sequence of word characters or '

import re

def first_word(text: str) -> str:
    return re.findall(r"\b[\w']+\b", text)[0]
#-----------------------------------------------------------

def first_word(text: str) -> str:
    word_beginning, word_end = None, None
    for index, symbol in enumerate(text):
        if word_beginning is None and symbol.isalpha():
            word_beginning = index
        if word_beginning is not None:
            if symbol.isalpha() or symbol == "\'":
                continue
            else:
                word_end = index
                break
    return text[word_beginning:word_end]
#-----------------------------------------------------------

def first_word(text: str) -> str:
    text_sliced = list(text)
    word = []
    for i in range(len(text_sliced)):
        if text_sliced[0].isalpha() or (text_sliced[0] == "-" or text_sliced[0] == "'") and len(word) > 0:
            word.append(text_sliced.pop(0))
        elif len(word)== 0:
            del text_sliced[0]
        else:
            break
    if len(word)>0:
            return ("".join(word))
#-----------------------------------------------------------

def first_word(text: str) -> str:
    # your code here
    i = 0
    res = ''
    flag = 0
    while i < len(text):
        if 'a'<=text[i]<='z' or 'A'<=text[i]<='Z'  or text[i] == "'":
            res += text[i]
            flag = 1
        else:
            if flag == 1:
                break
        i += 1
    return res
#-----------------------------------------------------------

import re
def first_word(text: str) -> str:
    return (re.search("[A-Za-z']+", text)).group()
#-----------------------------------------------------------

import re


def first_word(text: str, /) -> str:
    text = re.sub("[.,]", " ", text)
    text.split()
    return text.split()[0]
#-----------------------------------------------------------

def first_word(text: str) -> str:
    s1 = [".", ","]
    c = ''
    for i in range(len(text)):
        if text[i] not in s1:
            c += text[i]
        else:
            c += " "
    s = c.split()
    return s[0]
#...........................................................


