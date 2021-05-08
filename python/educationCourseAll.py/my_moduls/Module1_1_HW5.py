import os

def remdir(dirx):
    for i in range(1, int(dirx) + 1):
        dirn = 'dir_' + str(i)
        os.rmdir(dirn)