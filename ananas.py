import random

slots = [i + 1 for i in range(10)]  # просто слоты от 1 до 10
matrix = [[0 for _ in range(10)] for _ in range(10)]  # пустая матрица 10 на 10
matrix[0] = random.sample(slots, 10)  # рандомим первую строку


def not_vacant_list(slot, player_slots, matrix):
    '''возвращает список из уже занятых слотов в этой игре'''
    not_vacant = []
    temp = 0
    while temp != player_slots:
        not_vacant.append(matrix[temp][slot])
        temp += 1
    return not_vacant


def big_mistake(matrix, player_slots, slot):
    '''исправляет ошибки в рассадке'''
    zero = matrix[player_slots][slot]
    matrix[player_slots][slot] = 0
    while zero != 0:
        for temp in range(10):
            if zero not in not_vacant_list(temp, player_slots, matrix):
                matrix[player_slots][temp], zero = zero, matrix[player_slots][temp]

def generate(matrix):
    '''создает уже правильную рассадку'''
    for player_slots in range(1, 10):
        matrix[player_slots] = random.sample(slots, 10)
        for slot in range(10):
            if matrix[player_slots][slot] in not_vacant_list(slot, player_slots, matrix):
                big_mistake(matrix, player_slots, slot)


def create_table(matrix):
    '''привязвывает рассадку к никам'''
    generate(matrix)
    print('Введите ники')
    dir = {}
    for i in range(10):
        tmp = input()
        dir[tmp] = matrix[i]
    return dir

def show_for_players(players):
    '''показывает рассадку для игроков'''
    players = players
    for key, val in players.items():
        print(key, ":", *val)

def show_for_prist(players, game_num):
    '''показывает рассадку для конкретной игры'''
    dir = {}
    for nick, sits in players.items():
        dir[sits[game_num - 1]] = nick
    print('Игра', game_num)
    for i in range(1, 11):
        print(i, ':', dir[i])


def start(players):
    '''показывает по запросу нужную таблицу'''
    print('Показать таблицу для судей - 0, для игроков - 1')
    n = int(input())
    if n == 1:
        show_for_players(players)
    if n == 0:
        print("Введите номер игры")
        tmp = int(input())
        if 0 < tmp and tmp <= 10:
            show_for_prist(players, tmp)
        else:
            print("Такой игры нет")


players = create_table(matrix)
while True:
    start(players)
    print("Еще что то?(no)")
    if input() == "no":
        break