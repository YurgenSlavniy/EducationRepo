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

import pickle, json

my_favorite_crypto = {
    'name': 'GPB',
    'paers': ['GPB/USDT', 'GPB/XRP'],
    'prices': [{'date_pick':'Black_Monday','year':2021},
    {'date_pick':'сранькакаята','year':2345}]
}
# открываем файл на запись байт 'wb'
# метод picle
with open('favorit.picle', 'wb') as f:
    pickle.dump(my_favorite_crypto, f)

with open('favorit.json', 'w', encoding='utf-8'):
   jscrypto =  json.dump(my_favorite_crypto)
