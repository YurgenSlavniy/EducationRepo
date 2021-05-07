# """
# параметр ping - > функция выводит pong
# 2 параметра name и имя человека <Имя> - > функция приветствия пользователя
# параметр list показать содержтимое текущей директории
# """

import sys, os

def ping():
    print('PonG')

def hello(name):
    print('Приветствую ', name)

def get_info():
    print(os.listdir())

comand = sys.argv[1]

if comand == 'ping':
    ping()
elif comand == 'list':
    get_info()
elif comand == 'name':
    name = sys.argv[2]
    hello(name)