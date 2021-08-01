
def add_tagget_to_note():

    """добавляет вашу следующую цель в блокнот,
    добавляя эту цель в .txt файл к уже там сохранёным.
    и сохроняет файл"""

    with open('target_note.txt', 'a', encoding='utf-8') as f:
        with open('target_note.txt', 'r', encoding='utf-8') as fread:

            while True:
                next_target = input(f"\033[38mКакая ваша следующая цель? опишите её: ")
                if next_target == 'quit':
                    break
                f.write(f'{next_target}\n')

def targets_to_list():
    """Возвращает содержимое файсла с целями в виде списка целей"""
    with open('target_note.txt', 'r', encoding='utf-8') as fread:
        target_list = []
        for line in fread:
            target_list.append(line)
        return target_list

def all_targets_print():
    """Выводит все цели и нумирует их"""
    with open('target_note.txt', 'r', encoding='utf-8') as fopen:
        i = 0
        for line in fopen:
            i += 1
            print(f'ЦЕЛЬ № {i}: {line}', end='')

def hallo_yellow(hallo_text):
    """Делает приветственный текст жлтым"""
    print("\033[33m{}".format(hallo_text))

def red_attention(attention_text):
    """Делает подсказку по навигации. в крансом цвете"""
    print("\033[31m{}".format(attention_text))


#_________________________________________________________________
attention_text = '!!! - quit: для просмотра всех целей наберите quit !!!\n'
red_attention(attention_text)

hallo_text = 'Это блокнот выших целей.\nДобавляйте сюда свои цели\n'
hallo_yellow(hallo_text)


with open('target_note.txt', 'a', encoding='utf-8') as f:
    add_tagget_to_note()
#    print(f'\nВаши записи: {targets_to_list()} \n')

all_targets_print()