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