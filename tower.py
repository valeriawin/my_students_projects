import random
import time

# вывод предисловия
def display_intro():
    print("********************\nТы – Шрек, спасающий Фиону.\nСейчас ты находишься между 2 башнями.\nВ одной башне тебя ждет Фиона.\nА в другой – дракон, который за секунду тебя испепелит.\n********************\n")

# проверка правильного выбора башни
def choose_tower():
    tower_numb=input("Выбери башню (1/2): ")
    while tower_numb!="1" and tower_numb!="2":
        choose_tower()
    return int(tower_numb)

# кто тебе попадется?
def check_tower(chosenTower):
    print("Вы приближаетесь к башне.... ")
    time.sleep(2)
    print("Она темная и жуткая....")
    time.sleep(2)
    print("Перед тобой резко открывается дверь и из нее на тебя пристально смотрит...\n")
    time.sleep(2)
    rightTower = random.randint(1,2)
    if chosenTower==rightTower:
        print("Ты спас Фиону")
    else:
        print("Тебя сжег дракон")


# ниже идет сама игра
option = "yes"
while option == "yes":
    option=input("Сыграем? (yes/no) - ")
    if option == "yes":
        display_intro()
        check_tower(choose_tower())
        time.sleep(3)
