import os, sys

def directory_maker():
    print('начало работы функции')
    print(os.getcwd())
    print('Это текущая директория из которой запускается modul1. В которой он и расположен')
    os.mkdir('dir_1')
    os.mkdir('dir_2')
    os.mkdir('dir_3')
    os.mkdir('dir_4')
    os.mkdir('dir_5')
    os.mkdir('dir_6')
    os.mkdir('dir_7')
    os.mkdir('dir_8')
    os.mkdir('dir_9')

def directory_del():
    os.rmdir('dir_1')
    os.rmdir('dir_2')
    os.rmdir('dir_3')
    os.rmdir('dir_4')
    os.rmdir('dir_5')
    os.rmdir('dir_6')
    os.rmdir('dir_7')
    os.rmdir('dir_8')
    os.rmdir('dir_9')
#
# # directory_maker()
# # directory_del()
#
#
# ###
# # чужие решения:
# command = ''
# while command != 'выйти':
#     command = input('Введите действие ')
#     if command == 'создать':
#         dirx = input('Какое количество папок создать? ')
#         import creatdir
#         creatdir.creatdir(dirx)
#     if command == 'удалить':
#         print('Удаляю раннее созданные папки')
#         import remdir
#         remdir.remdir(dirx)
#     if command == 'список':
#         i = input('Введите ряд чисел через запятую ')
#         i = i.split(',')
#         import randomnum
#         r = randomnum.randomnum(list(i))
#         print(r)
#
# creatdir.py
#
# # import os
#
# def creatdir(dirx):
#     for i in range(1,int(dirx) + 1):
#         dirn = 'dir_' + str(i)
#         os.mkdir(dirn)
# # remdir.py
#
# import os
#
# def remdir(dirx):
#     for i in range(1, int(dirx) + 1):
#         dirn = 'dir_' + str(i)
#         os.rmdir(dirn)
# #----------------------------
# import os
#
# def new_p():
#     for i in range(1,10):
#         new_path = os.path.join(os.getcwd(), 'dir_{}' .format(i))
#         os.mkdir(new_path)
#
#
# def del_p():
#     for i in range(1,10):
#         new_path = os.path.join(os.getcwd(), 'dir_{}' .format(i))
#         os.rmdir(new_path)
# #----------------------------