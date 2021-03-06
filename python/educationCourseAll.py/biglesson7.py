# Урок 7 .
# ПОЛЕЗНЫЕ ИНСТРУМЕНТЫ. ОБРАБОТКА ИСКЛЮЧЕНИЙ.
# - тенарный оператор
# - генераторы списка и словарей
# - Принципы работы операторов and и or
# - Модуль copy
# - Обработка исключений

# Определение тернарного оператора
# применение
# синтаксис
# Примеры использования

# Тернарный оператор (ternarius - "тройной") оператор -
# операция, возвращающая свой первый или ретий операнд
# в зависимости от значения логического выражения,
# заданного вторым операндом

# мы будем возвращать РЕЗУЛЬТАТ 1 если выражение_истино иначе РЕЗУЛЬТАТ 2
# Применение:
# вместо констркций if ... else в которой нету elif
# вариантов всего 2 : либо условие истино, либо условие ложно
# позволяет писать компактный и читаемый код
# синтаксис:

is_has_name = True
name = 'Max' if is_has_name else 'Empty'
print(name)
# У нас есть переменная is_has_name которая равняется истине
# в переменную мы присвоим МАХ,
# если условие is_has_name else - ИСТИННО
# иначе присвоим 'Empty'
#  если поменяем условие is_has_name = False
#  будет выводить 'Empty'
#  Этот тернальный оператор заменяет нам if - else

is_one = False
number = 1 if is_one else 2
print(number)
# в переменную number мы присвоим единицу,
# если условие is_one, иначе присваиваем 2
is_russian = True
print('привет' if is_russian else 'Hello')
# напичатаем привет если условие - is_russian - истинно,
# иначе печатаем не порусски
# РЕЗУЛЬТАТ 1 если выражение_истино иначе РЕЗУЛЬТАТ 2

# Примеры использования:
# - переход от if к тернальному оператору
# У нас имеется некоторое слово --> СлОвО
# переводим какие то буквы в верхней регистр,
# какие то в нижний, чтобы они чередовались.

word = 'слово'
# для начала напишем алгоритм нашими простыми средствами,
# будем использовать циклы и обычные условные операторы.
# Затем заменим условные операторы на тернальные
# создаём переменную под результат result
result = []
# в результате хронятся переведёные буквы
for i in range(len(word)):
    if i%2 != 0:
        letter = word[i].lower()
    else:
        letter = word[i].upper()
    result.append(letter)
result = ''.join(result)
print(result)
# нам понадобится здесь индекс,
# для того чтобы можно было определять чётная буква или нечётная,
# поэтому воспользуемся циклом по длине слова .
# После того как записали цикл мы можем проверить
# чётная буква или нет.
# if i%2 == 0
# Если индекс нашей буквы делится на 2 без остатка, значит буква чётная.
# мы будем её переводить в нижний регистр:
# letter = word[i].lower()
# берём букву из слова по индексу и используем функцию lower()
# иначе буква нечётная и мы будем приводить её к верхнему регистру
# letter = word[i].upper()
# добавляем в результирующий список нашу букву
# result.append(letter)
# Из списка нужно сделать строчку по итогу.
# Можно воспользоваться методом join
# result = ''.join(result)
# таким образом мы сохраняем в спиаок по одной букве,
# с помощью метода join(result) сделаем строку
# чтобы поменять буквы  if i%2 == 0 меняем условия.

# Теперь ппытаемся оптимизировать имеющийся код:
# Попробуем заменить условный оператор if - else на тернальный
# letter = letter.lower() if i%2 == 0 else letter.upper()

word = input('Введите ваше слово')
result = []
for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i%2 == 0 else letter.upper()
    result.append(letter)
result = ''.join(result)
print(result)

# - сразу пишем тернальный оператор
# на примере программы проверка пароля пользователя.
password = input('Введите пароль: ')
print('Войти' if password == 'qwerty' else 'Неверный пароль')
# сразу пишем конструкцию принт
# и в ней используем тернальный оператор

# Генератор списков и словарей
# - определение генератора
# - примененеие генераторов
# - синтаксис
# - приемущества и недостатки
# - примеры
#
# в пайтон существует специальная синтаксическая конструкция,
# которая позволяет по орпределенным правилам создавать
# заполненные списки.
# Такие конструкции - генераторы списков.
# генераторы словарей по аналогии.
#
# применение:
# вместо цикла for
# позволяет писать компактный и читаемый код
# работают быстрее цикла for

# Синтаксис
# [number for number in numbers if number > 0]
# первым параметром идёт то, что мы записываем в список number
# дальше идёт цикл, типа цикла for. for number in numbers
# в конце может быть условие при котором
# мы записываем элемент в список если оно истино,
# если ложно элемент в список не пишем

# записать в список только положительные числа
numbers = [1, -1, 9, -8, 87, -65]
# классический способ
result = []
# создаём переменную для результата
for number in numbers:
# в цикле перебираем наши числа
    if number > 0:
# если число больше нуля
        result.append(number)
# в результат мы добавляем это число
print(result)
# выводим результат

# через функцию filter
result = filter(lambda number: number > 0, numbers)
# мы вызываем фуккцию filter, кторая состоит из двух частей
# второй параметр наш список numbers
# первый параметр - функция которая указывает записывать число в список или нет
# lambda number: number > 0
# это лямбда функция.
# на входе число number, на выходе number > 0
print(list(result))

# через генератор
result = [number for number in numbers if number > 0]
# в середине у нас находится цикл for number in numbers
# мы перебираем наш список чисел
# слева находится переменная которую мы будем добавлять в список - number
# справа находится условие по которому мы записываем переменную в список
print(result)

# генератор словаря похож на генератор списка
# но используется достаточно редко
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
# список который состоит из кортежей
# в которых есть число и какая то строка.
# Необходимо из этих кортежей создать словарь

# классический способ
result = {}
# создаём переменную под результат
for pair in pairs:
# перебираем пары, которые у нас лежат в списке.
# Каждая пара будет картежем
    key = pair[0]
# ключём будет первая часть картежа
    val = pair[1]
# значением будет вторая часть картежа
    result[key] = val
# в словарь по ключю key мы сохраняем значение val
print(result)

# через генератор словаей
result = {pair[0]:pair[1] for pair in pairs}
print(result)
print(type(result))
# for pair in pairs - мы перебираем пары в цикле
# в ответ мы записываем слева ключ pair[0], справа значение pair[1]
# тип результата словарь т.к гениратор записан в фигурных скобках

# преимущества
# - компактный и читаемый код
# - скорость
# недостатки:
# - нельзя заменить очень слжные конструкции
# - при ниправильном использовании могут наоборот ухудшить читаемость

# примеры:
# создать список из случайных чисел от 1 до 100
import random
# импортируем модуль random
# который позволит создавать случайные числа
# Объявляем переменную numbers, дальше будем создавать список numbers = []
numbers = [random.randint(1, 100) for i in range(10)]
# в списке будем генерировать случайное число
# с помощью random.randint(1, 100)
# число у нас будет от 1 до 100
# после этого нам надо организовать цикл.
# Например мы будем создавать 10 случайных ичисел
# for i in range(10)
# для этого воспользуемся счётчиком и функцией range
print(numbers)

# создать список квадратов чисел
numbers = [1, 2, 3, -1, -4]
numbers = [number**2 for number in numbers]
print(numbers)

# в генераторе не обязательно использовать условие if
# он может состоять всего из 2ух частей
# из цикла for number in numbers
# и значения которое мы запишем в список number**2

# создать список имен на букву А
names = ['Руслан', 'Амина', 'Дмитрий', 'Ариадна']
names = [name for name in names if name.startswith('А')]
print(names)
# в список будем записывать имя, которое у нас есть в цикле,
# но при условии если оно начинается на букву А
# Если условие истино - записываем в список, если ложно пропускаем
# если вообще условие не выполнится - получим пустой список.

# Принципы работы операторов and и or
# - привдение типов к bool в python
# - Python - стиль записи логических выражений
# - как работает and
# - как работает or
# - примеры применения
#
# привдение типов к bool в python
# Все встроенные типы данных в пайтон
# приводятся к логическому типу bool по определённым правилам
# истина:'abc', [1], (1,), {1:'a'}, 10, 1,1
# Истинной считается не пустая строка,
# непустой список, непустой кортеж, словарь
# число не равное 0, число с плавающей точкой и др...
# Ложь:'',[],{},0, None
# ложью считается пустая строка, список, кортеж, словарь,
# число ноль, тип None
#
# стиль записи логических выражений
# из за данного преобразования типов в
# пайтон желательно использовать локаничный стиль записи
# логических выражений
# вместо if len(str_var) > 0: ... когда мы проверяем длину строки
# пишем: if str_var:  мы можем написать если с указанием этой строки
# Это ускоряет разработку и делает код более читаемым
# строка
s = 'abc'
# классический способ
if len(s) != 0:
    print('Cтрока не пустая')
else:
    print('Строка пустая')
# удобный пайтон способ
# данный способ является более локаничным и логичным
# работает он благодоря тому, что
# не пустая строка - это истина,
# пустая строка - ложно
if s:
    print('Cтрока не пустая')
else:
    print('Строка пустая')
# Аналагично со списками, словарями и другими типами


l = (1, 2, 3)
d = {1:'a'}
# классический способ
if len(l) != 0 and len(d) != 0:
# берём длину списка и проверяем, что она не равна нулю len(l) != 0
# берём длину словаря и она тоже не должна быть равной 0 len(d) != 0
    print('Список и словарь не пустые')
# при этом условии словарь и список не пустые. выводим сообщение
else:
# иначе (если длина = 0) - они пустые
    print('Список и словарь пустые')


# удобный пайтон способ
if l and d:
#  Если список и если словарь, то они не пустые.
    print('Список и словарь не пустые')
else:
# иначе - пустые списки это None
    print('Список и словарь пустые')

# Как работает end Оператор and
# - не проверяет следующее логическое выражение,
# если текущее False (Ленивый)
# - оператор and возвращает первый ложный
# элемент или последний истинный
import math
if 1 > 2 and math.sqrt(-1):
# условие 1 > 2 заведомо будет равняться False,
# второе условие - возьмём квадратный корень из -1
# math.sqrt(-1)
# если вспомнить математику квадратный корень
# из отрицательных не извлекается
# и в этой строчке должна быть ошибка,
# но при такой постановки условий ошибки не будет,
# потому что пайтон как только проверит первое условие 1 > 2
# оно у нас ложь False
# уже всему выражению присвоит ответ False
# и далее условие не будет выполняться math.sqrt(-1)
    print('Ошибки не будет. т.к первое условие ложь')
# программа не сломается и мы пойдём дальше
print('двигаемся дальше')

# if math.sqrt(-1) and 1 > 2:
#   print('Если поменять местами то будет ошибка')
# пайтон сначала будет выполнять math.sqrt(-1)
# и здесь у нас возникнет ошибка.

# первая ложь у нас есть
# непустой список, пустой список, пустая строка , и единичка
print([1] and [] and '' and 1)
# питон нам вернёт первую ложь -
# [] - это пустой список .
# что питон воспринимает как ложь
# питон возвращает первое ложное условие в ряде end-ов

# Если же все условия истиные,
# питон вернёт последнюю истину
# последняя истина
print([1] and 1 and 20 and 1.1)

# Как работает or
# - Оператор or не проверяет следующее логическое выражение
# если текущее True (ленивый)
# - Оператор or возвращает первый истинный элемент
# или последний ложный
if 2 > 1 or math.sqrt(-1):
    print('Ошибки не будет. т.к первое условие истина')
# как только оператор or найдёт истину,
# дальше он проверять не будет
# и не дойдёт до проверки math.sqrt(-1)
# и не будет ошибки .
# Выйдем сразу после первой же правды

# первая истина
# в данном случае or вернёт 8
print(0 or [] or 8 or 5)
# последняя ложь,
# вернётся () - пустой кортеж
print(0 or [] or {} or ())

# примеры применения
# - and: извлечение квадратного корня из отрицательного числа
# - or: сохранение в переменную одного из 2-х значений

# есть список чисел
numbers = [1, 2, 5, -2, 9, -4, 3]
# создать список из тех чисел
# которые имеют квадратный корень меньше 2
# [1, 2, 3] - такой список должен получиться
result = []
# обычный способ
for number in numbers:
    if number > 0:
        sqrt = math.sqrt(number)
        # квадратный корень меньше 2
        if sqrt < 2:
            result.append(number)
print(result)

result = []
# через ленивый end
for number in numbers:
    if number > 0 and math.sqrt(number) < 2:
        result.append(number)
print(result)
# через генератор
result = (number for number in numbers if number > 0 and math.sqrt(number) < 2)
print(result)

# добавление элемента в список
# классический способ
def add_to_list(input_lst=None):
# параметр input_lst=None
    if input_lst is None:
# если параметр остаётсся None
# вызываем функцию с пустым параметром add_to_list()
        input_lst = []
# тогда создаётся список
    input_lst.append(2)
# и в список добавляется элемент - 2
    return input_lst
# возвращаем список.
# Должен получится список с одним элементом - 2

# Если же наш список не равен none,
# это означает что функция вызвана с параметром.
# и уже в параметре есть список
# Тогда условие if input_lst is None НЕ ВЫПОЛНЯЕТСЯ -
# не создаётся новый лист. input_lst = [],
# а просто добавляется элемент
# в конец списка в итоге возвращаем список 1. 2. 3

# пример вызова функции с параметром.
# в параметре - список!
result = add_to_list([0, 1])
print(result)
# пример вызова функции без параметра
result = add_to_list()
print(result)

# через or
def add_to_list(input_lst=None):
# используем свойство or вместо условия
# вместо конструкции if
    input_lst = input_lst or []
# переменная равняеется input_lst - списку или пустому списку.
# как это работает?
# Если input_lst останется None
# т.е мы вызвали функцию без параметров
# result = add_to_list()
# input_list будет None или пустой список
# input_lst or []
# и в результате нам вернётся пустой список
# и далее в него мы добавим элемент
# Если же функция будет вызвана с параметром
# т.е input_list не будет None -
# ответ будет текущий список,
# мы его просто пересохроним в переменную
# и добавим к списку новый элемент
# input_lst.append('element')

    input_lst.append('element')
    return input_lst

# пример вызова функции с параметром.
# в параметре - список!
result = add_to_list(['ИЕ', 1, 'ey', 2])
print(result)
# пример вызова функции без параметра
result = add_to_list()
print(result)

# Модуль Copy
# - Хранение спсиков в памяти
# - Изменение элементов списка в функции
# - копирование списка
# - модуль copy

# Хранение списков в памяти
# - при работе со списками помнить о том,
# что если мы переписываем список в другую переменную a = b
# а потом меняем значения внутри нового списка b[1],
# то значение изменится и внутри старого списка a[1]
# т.к ссылки на элементы списка остаются на своих местах
# в памяти и каждый список использует одни и теже элементы
# у списков a и b будет один ай ди в памяти, и меняя что то в одном,
# меняется и в другом списке
# аналогия с числом
a = 10
b = a
b = 100
print(a, b) # число a не изменилось
# работа со списком
a = [1, 2, 3]
b = a
b[1] = 100
# список а тоже изменился вместе с b
print(a, b)

# Изменение элементов списка в функции
# при передаче списка параметром в функцию
# нужно быть особенно внимательными
# т.к функция может изменить элемент списка
# внутри основной программы
numbers = [1, 2, 5, 15, 26]
def change_number_in_list(input_list):
    input_list[0] = 200
# после вызова функции
change_number_in_list(numbers)
# список в основной программе тоже изменился
print(numbers)
# чтобы этого избежать необходимо работать с копией списка

# методы копирования списка
# - создание среза от начала и до конца списка my_list[:]
b = numbers[:]
# - метод copy у самого списка
# примеры

a =[1, 3, 5, 6, 7]
b = a[:]
b[1] = 456
print(a, b)

# копия с помощью метода copy
b = a.copy()
b[1] = 254
print(a, b)
# !!! Эти способы не будут работать если есть вложенные списки
# a = [1, 2, [1, 2]]
# b = a[:]
# b[2][1] = 200
# список a снова меняется
# print(a)
# b = a.copy()
# b[2][1] = 200
# список a снова меняется
# print(a)
# потому что срез копирует только первую часть списка
# и не учитывает вложенность

# Модуль copy применяется для полного(глубокого)
# копирования списка
# используется модуль deepcopy
# b = copy.deepcopy(a)
import copy
# импортируем встроенный в пайтон модуль
a = [1, 4, [4, 6]]
b = copy.deepcopy(a)
# из модуля copy вызываем функцию deepcopy,
# куда аргументом идёт наш список deepcopy(a)
b[2][1] = 234
# меняем в элементе с индексом 2 - [4, 6]
# меняем элемент с индексом [1]
print(a, b)

# Обработка исключений
# - определение исключительной ситуации
# - обработка исключений
# - примеры
# - Генерация исключений

# исключительная ситуация.
# во время выполнения программы могут возникать ситуации,
# когда состояние внешних данных, устройств ввода-вывод
# или компьютерной системы в целом делает дальнейшие вычисления
# в соответствии с базовым
# алгоритмом невозможным или бессмысленными

# классические примеры
# - деление на ноль
# - корень квадратный из отрицательного числа
# - ошибка чтения данных при отсутствии доступа к ресурсу

# обработка исключений
# - что делать при возникновении исключительной ситуации?
# - Как опредилить произошла ли исключительная ситуация
# или программа работает в нормальном режиме
# - пайтон имеет встроенный механизм обработки исключений
# для того чтобы отработать исключительнуюситуацию,
# код который может её сгенерировать
# мы должны положить в блок try:
# блок с возможной исключительной ситуацией
# если вдруг в этом блоке возникнет исключительная ситуация,
# то действие которое мы будем делать пo её обработки
# мы кладем в блок expect
# expect:
number = int(input('Введите число'))
result = 100 / number
# если пользователь вводит 0,
# программа падает и мы получаем ошибку
# ZeroDivisionError: division by zero
# нам нужно проработать ситуацию,
# если пользователь вводит 0
number = int(input('Введите число'))
try:
    result = 100 / number
except:
    print('на ноль делить нельзя!')
# етперь пользователь если вводит 0
# возникнет исключительная ситуация
# но программа не останавливается и не вылетает ,
# мы переходим в блок expect

# Перехват конкретных исключений
# - в пайтон каждая исключительная ситуация имеет свой тип:
# TypeError, ValueError,...
# самое общее исключение имеет тип Exception
# Рекомендуется обрабатывать конкретные исключительные ситуации
# и реагировать на разные исключения по разному
number = int(input('Введите число: '))
try:
# в блоке try мы обрабатываем исключительную ситуацию
    result = 100 / number
# при указании except пишем возможный вариант ошибки
except ZeroDivisionError:
# мы знаем пользователь может ввести 0
# и тогда у нас будет исключительная ситуация
# и пользователь увидит соответствующее сообщение
    print('Попытка деления на 0')
except Exception:
# этот класс у нас имеют самые общие ошибки
    print('Неизвестная ошибка')

# теперь когда мы вводим 0 мы попадаем в блок ZeroDivisionError
# если возникнет какая нибудь другая исключительная ситуация
# мы попадём  в блок Exception

# Информация об ошибке
# можно получить дополнительную информацию об исключении если использовать конструкцию
# except название_исключения as e:
# тогда в переменную e будет сохранён объект исключения
# и мы сможем посмотреть данные по этому объекту
number = int(input('введите число'))
try:
    result = 100 / number
except ZeroDivisionError as e:
    print('попытка деления на 0')
    print('информация об исключении:', e)
except Exception as e:
    print('Неизвестная ошибка')
    print('информация об исключении:', e)

# try - expect - else - finaly
# расширенный вариант конструкции try - expect
# блок try - код который может вызвать исключение блок except
# - что делать при возникновении исключения блок else
# - что делать если исключения не произошло
# блок finally - выполняется всегда, если ошибка была и если её не было
number = int(input('введите число'))
try:
# код который может вызвать исключительную ситуацию
    result = 100 / number
except:
# что делать если возникла исключительная ситуация
    print('деление на ноль')
else:
# что делать если ошибок не было
    print('все хорошо ошибок не было')
finally:
# выполняется всегда
    print('что делаем когда есть ошибка и когда её нет')

# Генерация исключений иногда требуется не обработать
# а наоборот создать исключительную ситуацию
# Это можно сделать с помощью команды raise.
# raise Exception('Что то пошло не так')
# мы вызываем команду raise
# и указываем тип исключительной ситуации
# которую хотим создать
print('начало')
raise Exception('Что то пошло не так')
# текст исключительной ситуации
print('конец')

# при запуске команда остановится, когда наткнётся на raise
# и выдаст ошибку с текстом который мы ввели
#  raise Exception('Что то пошло не так')
# Exception: Что то пошло не так
# класс общий Exception:
# и в конец программы мы уже не попадаем. прога вылетает
# можем обработать исключение с помощью средств. которые мы прошли ранее
