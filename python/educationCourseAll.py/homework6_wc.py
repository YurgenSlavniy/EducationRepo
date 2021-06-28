# создать модуль music_serialize.py.
# В этом модуле определить словарь для вашей любимой группы, например:
# my_favourite_group = {'name': 'Aqua.'tracks':['Roses are Red','Barbie Girl'],
# 'albums':[{'name':'Aquarium','year':1997},{'name':'Aquarius','year':2000}]}
# C помощью модулей json и pickle сериализовать данный словарь в json и в байты,
# вывести результаты в терминал записать результаты в файлы
# group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8

# создал директорию homework6_wc в которую поместил 2 файла: music_serialize.py и music_deserialize.py
# работаем в модуле music_serialize.py

# импортируем модуль
import json
# импортируем следющий модуль
import pickle

# создаём словарь
my_favourite_group = {'name': 'Aqua.', 'tracks':['Roses are Red','Barbie Girl'],
                      'albums':[{'name':'Aquarium','year':1997},{'name':'Aquarius','year':2000}]}
# в словаре храним информацию о группе : её название - 'name': 'Aqua.' ,
# песни которые написала группа : 'tracks':['Roses are Red','Barbie Girl']
# и альбомы 'albums':[{'name':'Aquarium','year':1997},{'name':'Aquarius','year':2000}]}
# в альбоме также присутствует год выпуска и название 'year':1997. 'name':'Aquarium'
print(my_favourite_group)
print(type(my_favourite_group)) # <class 'dict'>

# нам нужне сериализовать этот словарь, вывести результаты на экран, и в файлы.
# Будем это делать с помощью модулей json и pickle . сделаем его импорт : import json
# начинаем работу с модулем json:
j_group = json.dumps(my_favourite_group)
# сначала выведем результаты на экран. Дадим имя j_group ,
# чтобы обозначить переменную для нашей группы,
# которая у нас будет в формате json. И вызываем функцию json.dumps
# для того чтобы сразу привести словарик к формату json
# параметром передаём (my_favourite_group)

# выведим результат на экран
print(j_group)
print(type(j_group)) # <class 'str'>
# Хотя вывод практически не изменился, но поменялся тип данных .

# проделаем похожую вещь с помощью модуля pickle
p_group = pickle.dumps(my_favourite_group)
print(p_group)
print(type(p_group)) # <class 'bytes'>
# методы называются динаково как в модуле json так и в модуле pickle
# После метода .dump в модуле pickle мы видим набор байт

# теперь сохраним данные в файл.
# для этого достаточно воспользоваться другими функциями модулей json pickle
# для начала откроем файл.
# будем пользоваться менеджером контекста with

with open('group.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(my_favourite_group, jsonfile)
# файл json мы открываем на запись  'w' и указываем кодировку encoding='utf-8'
# далее после того, как файл открыт используем модуль json
# json.dump(my_favourite_group, jsonfile)
# первый параметр это наш словарь - my_favourite_group,
# второй параметр - jsonfile -  имя файла.

# запускаем файл и в папке homework6_wc
# где наш music_serialize.py
# появляется файл group.json
# Если его открыть через пайчарм
# мы увидим нашу группу сохранёную в json формате

# сделаем похожее действие для модуля pickle:
with open('group.pickle', 'wb') as picklefile:
    pickle.dump(my_favourite_group, picklefile)
# открываем файл 'group.pickle'
# открываем файл на запись байт 'wb',
# поэтому кодировку указывать не нужно
# мы создаём второй файл и запишем туда набор байт
# Мы сделали вывод в терминал и запись информации в файл #


# ВТОРАЯ ЧАСТЬ ЗАДАНИЯ
# Создать модуль music_deserialize.py
# В этом модуле открыть файлы group.json и group.pickle
# прочитать из них информацию
# Получить объект словарь из предыдущего задания

# Создать модуль music_deserialize.py
# В этом модуле открыть файлы group.json и group.pickle
# прочитать из них информацию
# Получить объект словарь из предыдущего задания

# мы используем 2 файла, чтобы смодулировать ситуацию,
# когда например один разработчик записывает данные в файл
# и передаёт другому разработчикутакже данные
# можно например вместо вывода в терминал передовать по сети.
# Импортируем модули json и pickle
import json
import pickle
# далее открываем файл
with open('group.json', 'r', encoding='utf-8') as jsonfile:
    result = json.load(jsonfile)
# открываем файл 'group.json'
# на чтение 'r'
# указываем кодироку encoding='utf-8'
# ту же самую кодировку в которой мы записывали файл
# после того как файл открыт ,
# создаём переменную в которую мы будем читать результат
# result =  используем метод json и метод load
# и передаём в него параметр jsonfile название файла

# после того как мы получили результат проверим,
# что у нас он совпадает с тем, что был изначально
print(result) # <class 'dict'>
print(type(result))

# теперь используем
# модуль pickle похоже на метод json
# но мы работаем с байтами
with open('group.pickle', 'rb') as picklefile:
    result = pickle.load(picklefile)
print(result) # <class 'dict'>
print(type(result))
# открываем файл 'group.pickle'
# на чтение байт 'rb'
# Объявляем переменную result
# и используем метод .load