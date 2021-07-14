def try_to_move(i,a,b,moves):
    if i == moves[0]:
        a+=1
    elif i == moves[1]:
        a-=1
    elif i == moves[2]:
        b+=1
    elif i == moves[3]:
        b-=1
    else:
        print("Ошибка ввода!")
###############################
def proverka(a,b):
    print("я тут")
    if a >= 0:
        print(a,"шагов в вверх")
    if a <= 0:
        print(a,"шагов вниз")
    if b >= 0:
        print(b,"шагов в вправо")
    if b <= 0:
        print(b,"шагов в влево")
################################
moves = ["вверх","вниз","вправо","влево","проверка"]
print(moves)
i = input("Введите куда двигаться: ")
a = 0
b = 0
while i != moves[4]:
    try_to_move(i,a,b,moves)
    i = input("")
proverka(a,b)
