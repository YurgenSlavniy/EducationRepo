# Практикум. Игра угадай число.
# компьютер загадывает случайное число от 1 до 100
# Пользователю предлагается его угадать
# Если пользователь угадал, программа сообщает о победе
# Если пользователь ввёл неверно число, программа даёт ему подсказку: ввведёное число больше или меньше заданного
# Будем разбивать задачу на шаги и постепенно её реализовывать
# наш первый шаг: Программа загадывает нам случайное число.
# мы воспользуемся встроенным в питон модулем - рандом.
import random # импортируем модуль рандом
number = random.randint(1, 100) # создаём переменную, где у нас будет хрониться наше случайное число
# в модуле рандом вызываем функцию рэндинт random.randint(1, 100)
# у функции randint(1, 100) есть 2 параметра: от кокого и до какого числа мы хотим сгенерировать случайное число

#  2: пользователю предлагают угадать число
# предпологается пользователь введёт число с клавиатуры
# Объявляем переменную и через инпут запрашиваем пользователя ввести число.
user_number = int(input('Угадайте число от 1 до 100: '))
# В этой переменной будет хрониться число, которое введёт пользователь
# Т.К. input нам даёт строку, не забываем её привести в числовой класс int

# Шаг 3: Сравнить введёное число с загаданным и вывести результат.
# Если число совпадает с загаданным - победа.
# Если число не совпадает - подсказка
if number == user_number:
    print('Ура!! Победа!! Число угадано!!')
elif number < user_number:
    print('вы ввели число больше, чем загадал компьютер')
else:
    print('вы ввели число меньше, чем загадал компьютер')
# воспользуемся условиями if  : если числа совпали - выводим победу.
# elif - условие: если загаданное чисо меньше - выводим подсказку меньше
# else - условие: если загаданное чисо больше - выводим подсказку больше
# т.к. у нас 3 варианта ответа. больше, меньше, равно, то условия if elif else

# шаг 4: реализовать цикл
# чтобы игра продолжалась, пока пользователь не отгадает число.
# самый простой способ - организация бесконечного цикла
while True:
    user_number = int(input('Угадайте число от 1 до 100: '))
    if number == user_number:
        print('Ура!! Победа!! Число угадано!!')
        break
    elif number < user_number:
        print('вы ввели число больше, чем загадал компьютер')
    else:
        print('вы ввели число меньше, чем загадал компьютер')

# таким образом всё что находится в цикле будет постоянно повторяться, пока не угадаем число и не попадём на команду break

number = random.randint(1, 100)
user_number = None
# Нам надо добавить в игру уровни сложности
# Чем выше уровень сложности, тем меньше попыток даётся пользователю, чтобы угадать число.
# Но сперва немного улучшим цикл while
# Бесконечный цикл это хорошо, но лучше выходить из цикла по условию
# это условие number == user_number
while number != user_number: # условие цикла - пока загаданное число не равно числу введёному полльзователем
    user_number = int(input('Угадайте число от 1 до 100: '))
    if number < user_number:
        print('вы ввели число больше, чем загадал компьютер')
    elif number > user_number:
        print('вы ввели число меньше, чем загадал компьютер')
print('ПОБЕДА!')
# Если if и elif условия не выполнятся, Значит число равняется юзернамбер, мы выходим из уикла и пишем победа.
# Остаётся только задать начальное значение для user_number, это делается перед циклом
# user_number = None, чтобы первый раз прошла проверка и мы вошли в цикл.

# Добавим в игру количество попыток.
number = random.randint(1, 100)
user_number = None
count = 0 # введём новую переменную чтобы учесть число попыток.
# присвоим значение для этой переменной 0, потому что пользователь ещё не сделал ни одной попытки.
max_count = 8 # максимальное количество попыток указываем  в этой переменной
while number != user_number: # условие цикла - пока загаданное число не равно числу введёному полльзователем
    count += 1 # В цикле мы будем увеличивать эту переменную на 1
# для того чтобы учитывать сколько раз пользователь ввёл число
    if count > max_count:
        print('Вы проиграли! Попытки закончились')
        break
    print (f'Попытка № {count}') # Выводим пользователю сообщение о числе попыток
    user_number = int(input('Угадайте число от 1 до 100: '))
    if number < user_number:
        print('вы ввели число больше, чем загадал компьютер')
    elif number > user_number:
        print('вы ввели число меньше, чем загадал компьютер')
else:
    print('ПОБЕДА!')
# Для ограничения количества попыток добавим новую переменную
# max_count - максимальное количество попыток
# while - else. Иначе слово Победа будет печататься при выходе из цикла по брейку
# а убрав его в эту конструкцию при поражении будет только слово о поражении

# Добавление уровней сложности, выбор уровня сложности.
# Уровни сложности удобнее всего хронить в словаре.
# объявляем словарь levels
#
number = random.randint(1, 100)
user_number = None
count = 0
levels = {1: 25, 2: 17, 3: 13, 4: 8 , 5: 5}
# создаём словарик для уровней сложности, в котором будем хронить ключи - названия уровня, а значение будет количество попыток
max_count = levels[3] # теперь переменной макскаунт мы присваиваем levels[3].
# По ключу 3, мы определяем количество попыток - 13.
# т.е значение max_count становится равным 13. по ключу 3:13

while number != user_number:
    count += 1

    if count > max_count:
        print('Вы проиграли! Попытки закончились')
        break
    print (f'Попытка № {count}')
    user_number = int(input('Угадайте число от 1 до 100: '))
    if number < user_number:
        print('вы ввели число больше, чем загадал компьютер')
    elif number > user_number:
        print('вы ввели число меньше, чем загадал компьютер')
else:
    print('ПОБЕДА!')
#
# Остаётся только сделать так, чтобы пользователь вначале игры выбирал уровень сложности.
#
number = random.randint(1, 100)
user_number = None
count = 0
levels = {1: 25, 2: 17, 3: 13, 4: 8 , 5: 5}

level = int(input('Выбор уровня сложности от 1 до 5: ')) # создаём переменную левел,
# эта переменная будет ключом в словаре levels
max_count = levels[level] # в качестве ключа подставляем переменную
while number != user_number:
    count += 1

    if count > max_count:
        print('Вы проиграли! Попытки закончились')
        break
    print (f'Попытка № {count}')
    user_number = int(input('Угадайте число от 1 до 100: '))
    if number < user_number:
        print('вы ввели число больше, чем загадал компьютер')
    elif number > user_number:
        print('вы ввели число меньше, чем загадал компьютер')
else:
    print('ПОБЕДА!')

# Следующая модификация - это игра для нескольких игроков.
# - добавить в игру выбор количества пользователей
# - добавить возможность ввода имен пользователей
# - добавить систему поочередного хода
# - добавить объявление победителя

number = random.randint(1, 100)
user_number = None
count = 0
levels = {1: 25, 2: 17, 3: 13, 4: 8 , 5: 5}

level = int(input('Выбор уровня сложности от 1 до 5: '))
max_count = levels[level]

# После выбора уровня сложности будем выбирать количество пользователей
player_count = int(input('Введите количество угадывающих: '))
# для этого создаём переменную и запрашиваем у пользователя ввести информацию
# для сохранения имён, нам хорошо подойдёт список
players = [] # для этого объявляем пустой список
# у нас есть количество player_count числа играющих, именно столько раз надо будет ввести имя игрока
# Организуем цикл:
for player in range(player_count):
    player_name = input(f'введите имя игрока {player}')
    players.append(player_name)
# Мы пбудем пробегать количество пользователей
# И просить играющих ввести имя игроков, присваиваем имя в переменную player_name
# Добавляем в пустой список введёное имя игрока, идём дальше по циклу

# шаг 2 - реализациия логики очерёдности хода (пользователи угадывают число по очереди)
# Нужно определиться с местом в коде где реализовавать решение
#
is_winner = False # Эта переменная будет обозначать что у нас есть победитель
winner_name = None # вторую переменную вводим winner_name и пока победителя нет присваиваем значение None

while not is_winner:
# меняем условия в цикле - пока у нас нет победителя:
# мы выполняем наши действия и идём в цикл for
    count += 1

    if count > max_count:
        print('Все игроки проиграли! Попытки закончились')
        break
    print (f'Попытка № {count}')
# функционал для количества игроков будем реализовавать здесь
# Теперь у нас пользователей много их будем перебирать в цикле
    for player in players:
        print(f'Ход игрока {player}')
# таким образом мы будем сначала перебирать пользователей в цикле for? а потом уже прибавлять номер попытки (выше)
        user_number = int(input('Угадайте число от 1 до 100: '))
# теперь после того ка кпользователь ввёл число мы сразу должны его проверить
        if user_number == number:
# если условие выполнено, это означает что игрок победил, у нас появился победитель
            is_winner = True
# далее сохроняем имя победителя
            winner_name = player
# делаем выход из цикла
            break
        elif number < user_number:
            print('вы ввели число больше, чем загадал компьютер')
        else:
            print('вы ввели число меньше, чем загадал компьютер')
else:
# для вывода победителя немного изменим выводное сообщение
    print(f'ПОБЕДА! {winner_name}')
# Для определения победителей необходимо переписать логику работы циклов.
# Цикл for перебирает всех пользователей, а цикл while сделает выход только тогда,
# когда каждый пользователь ввел число
# Если например первый пользователь угадал число, нам тут же надо выйти и объявить победителя.
# перед циклом while объявим переменную is_winner = False
# Эта переменная будет обозначать что у нас есть победитель
# вторую переменную вводим winner_name и пока победителя нет присваиваем значение None
#