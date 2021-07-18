# надо писать мысли и сюда... общение с самим собой.
# о коде.
# рассуждаю с собой в письменно-печатной форме.

# надо выдернуть номер

# надо добавить надпись в блокнот
def add_tagget_to_note():
    """добавляет вашу следующую цель в блокнот"""
with open('target_note.txt', 'a', encoding='utf-8') as f:
    with open('target_note.txt', 'r', encoding='utf-8') as fread:
        target_number = 0
        for line in fread:
            target_number += 1

    next_target = input("Какая ваша следующая цель? опишите её: ")
    f.write(f'\nЦель №{target_number} :{next_target}')


with open('target_note.txt', 'a', encoding='utf-8') as f:
        add_tagget_to_note()
with open('target_note.txt', 'r', encoding='utf-8') as f:
    print(f.read())

