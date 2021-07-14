#Представь, что ты герой видеоигры. Пользователь говорит тебе, куда двигаться
# (вверх, вниз, вправо или влево на 1 клетку). После нескольких движений, посмотри,
# насколько ты сместишься относительно начальной точки (выше/ниже на A клеток, левее/правее на B клеток)

def up_down():
    up = game.count(1)
    down=game.count(2)
    if up>down:
        up_down=up-down
        print(up_down, "вверх")
    elif up<down:
        up_down=down-up
        print(up_down, "вниз")
    else:
        print("ни вверх, ни вниз ;)")

def r_l():
    r = game.count(3)
    l=game.count(4)
    if r>l:
        r_l=r-l
        print(r_l, "напрво")
    elif r<l:
        r_l=l-r
        print(r_l, "налево")
    else:
        print("ни влево, ни вправо ;)")
#####################################################3

game = []
gamer = int(input("Привет, поиграем? Если согласен, нажми любую цифру, а 0 если пока не готов\n"))
if gamer == 0:
    print("Пока, пока")
while gamer != 0:
    gamer=int(input("Куда идем?\n"
                "1. Вверх\n" 
                "2. Вниз\n" 
                "3. Вправо\n" 
                "4. Влево\n" 
                "0. Остановиться"))
    game.append(gamer)
print(game, "\n твои шаги")
print(up_down(), r_l())