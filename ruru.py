import random

#создаем переменные со списками
players = []
bullets = []

#создаем список с пулями
for i in range(6):
    bullets.append('bullet')
no_bullet_idx = random.randint(0, len(bullets) - 1)
bullets[no_bullet_idx] = 'no'

#создаем список с игроками
players_count = int(input('Количество игроков'))
while players_count > 3:
    players_count = int(input('Количество игроков'))
for i in range(players_count):
    players.append(input('Введите имя игрока #' + str(i + 1) + ': '))

#создаем переменные
current_player = 0
taken = 0

#основной цикл игры
while taken < 6:
    
    if current_player > players_count - 1:
        current_player = 0
    print('Стреляет ' + players[current_player])
    input('Enter') 
    
    chosen_bullet = random.choice(bullets)
    bullets.remove(chosen_bullet)
    if chosen_bullet == 'bullet':
        print("Выстрел! Ты выбываешь. Игра окончена")
        break
    else:
        print("Все хорошо, ход переходит к следующему игроку")
    current_player += 1
    taken += 1
