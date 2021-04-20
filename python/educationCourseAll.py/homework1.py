# Практическое задание
# 1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран. Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.
# 2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.
# 3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.

# (Формула не соответствует реальной действительности и здесь используется только ради примера)
# Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.  Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно. В случае ошибок, уточните условия для той или иной ситуации.
# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

# 1. Запросить у пользовтеля число, сохранить в переменную, прибавить к числу 2, вывести результат на экран
a = int(input('Введите целое положительное число '))
a = a + 2
print('результат ', a)

# 2. Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше 10. После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.

number = int(input('Введите пожалуйста число'))

if number >= 10:
    print('Забыл предупредить число от 0 до 10')
else:
    print('Возвожу в степень 2 и получаю ', number**2)

print('вариант для программки с циклом')
number = int(input('Введите пожалуйста число'))
while number >= 10:
    print('Забыл предупредить число от 0 до 10')
    number = int(input('Введите пожалуйста число'))
print('Возвожу в степень 2 и получаю ', number ** 2)
print('---->')

# Медицинская анкета.
print('Medical questionnaire. Медицинский опросник')
print('---->')

name = input('What is name? Введите имя: ')
surname = input('What is surname? Введите фамилию: ')
age = int(input('How old ? Каков возраст?'))
mas = int(input('What is weigth? Сколько весит?'))

if age <= 30 and mas >= 50 and mas <= 120:
    print('Имя:', name, ', Фамилия:', surname, ', Возраст:', age, ', Вес:', mas, ' ---> Хорошее состояние ')
elif age > 30 and age < 40 and mas < 50 or mas > 120 and age > 30 and age < 40:
    print('Имя:', name, ', Фамилия:', surname, ', Возраст:', age, ', Вес:', mas, ' ---> Следует заняться собой ')
elif age >= 40 and mas <= 50 or mas >= 120 and age >=40:
    print('Имя:', name, ', Фамилия:', surname, ', Возраст:', age, ', Вес:', mas,' ---> Требуется врачебный осмотр ')
else:
    print('Имя:', name, ', Фамилия:', surname, ', Возраст:', age, ', Вес:', mas,)



