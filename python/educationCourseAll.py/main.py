playername = input('Введите имя игрока: ')
player = {'name': playername, 'health': 100, 'damage': 75}
enemy = {'health': 125, 'damage': 34}

def attack(person1, person2):
    person1 = player
    person2 = enemy
    fight = person2['health'] - person1['damage']
    if fight > 0 :
        person2['health'] = fight
        print(person2)
        return person2
    else:
        print('Враг Повержен!')


attack(player, enemy)

player['armor'] = 1.2
enemy['armor'] = 1.5
