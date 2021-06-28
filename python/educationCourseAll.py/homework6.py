# 1: Создать модуль music_serialize.py.
# В этом модуле определить словарь для
# вашей любимой музыкальной группы, например:
# my_favourite_group = {
# ‘name’: ‘Г.М.О.’,
# ‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
# ‘Albums’: [{‘name’: ‘Делать панк-рок’,‘year’: 2016},
# {‘name’: ‘Шапито’,‘year’: 2014}]}
# С помощью модулей json и pickle сериализовать данный
# словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle
# соответственно. В файле group.json указать кодировку utf-8.

# 2: Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

# для создания модуля я сперва создаю новую директорию,
# в которой буду уже создавать модули:
# import os
# new_path = os.path.join(os.getcwd(), 'homework6moduls')
# os.mkdir(new_path)
# и уже в директории homework6moduls. которая появилась в ЛП:
# ПКМ -> new -> python file
# Даём имя этому модулю - нашему создаваемому пайтон файлу
# music_serialize
# теперь у нас в папке (директории) 'homework6moduls' появился файл
# music_serialize.py - это наш модуль
# в модуле определяем, создаём словарик:

import pickle, json

my_favorite_crypto = {
    'name': 'GPB',
    'paers': ['GPB/USDT', 'GPB/XRP'],
    'prices': [{'date_pick':'Black_Monday','year':2021},
    {'date_pick':'сранькакаята','year':2345}]
}
# открываем файл на запись байт 'wb'
# метод picle
with open('favorit.picle', 'w') as f:
    pickle.dump(my_favorite_crypto, f)

with open('favorit.json', 'wb', encoding='utf-8'):
   jscrypto =  json.dumps(my_favorite_crypto)
#
#
#
#