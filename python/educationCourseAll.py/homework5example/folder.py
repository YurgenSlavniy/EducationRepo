import os

def create_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.mkdir(folder_name)

def delete_folders():
    for i in range(1, 10):
        folder_name = f'dir_{i}'
        os.rmdir(folder_name)

if __name__ == '__main__':
    create_folders()
    delete_folders()