# -*- coding: utf-8 -*-
import time
import datetime
import random
from tkinter import *
from getpass import getpass

from conversion import money
from admin import *


def credit():
    option = input("В нашем банке Вы можете оформить самые выгодные кредиты. \n Для Вашего удобства мы сразу рассчитаем переплату за весь срок кредитования и ежемесячные платежи \n Выберите наиболее понравившейся Вам вариант: \n 1. Кредит 'старт' для молодых семей \n 2. Кредит 'офицерский' для сотрудников ВС РБ \n 3. Заполнить анкету для предварительного рассмотрения \n ")
    if option == "1" or option == "семья":
        print("Данный кредит предназначен для молодых семей с процентной ставкой 45 % годовых, с правом досрочного погашения ")
        summa_credita = float(
            input("Введите сумму которую хотели бы рассчитать: "))
        x = summa_credita
        srok = float(
            input("Введите на какой срок (в месяцах) хотите получить кредит: "))
        n = srok
        procent = 45 // n
        i = procent
        pereplata = n*x*(i*(1+i)**n)//((1+i)**n-1)-x
        fam = pereplata // 100
        month_payment = x // n
        print(f"На выбранную сумму и срок переплата составит {fam} ")
        print(f"Ежемесячный платёж составит {month_payment}")

    if option == "2" or option == "офицер":
        print("Данный кредит для сотрудников силовых ведомств с процентной ставкой 50 % годовых, без права досрочного погашения")
        summa_credita = float(
            input("Введите сумму которую хотели бы рассчитать: "))
        x = summa_credita
        srok = float(
            input("Введите на какой срок (в месяцах) хотите получить кредит: "))
        n = srok
        procent = 50 // n
        i = procent
        pereplata = n*x*(i*(1+i)**n)//((1+i)**n-1)-x
        of = pereplata // 100
        month_payment = x // n
        print(f"На выбранную сумму и срок переплата составит {of}")
        print(f"Ежемесячный платёж составит {month_payment}")

    if option == "3" or option == "анкета":
        person_name = input("Введите ФИО: ")
        person_age = input("Введите Ваш возраст: ")
        person_experience = input("Введите трудовой стаж: ")
        person_children = input("Введите кол-во детей до 18 лет: ")
        person_summa = input("Введите сумму: ")
        person_month = input("Ведите срок: ")
        person_number = int(
            input("Выберите номер кредита 1. 'старт' или 2. 'офицерский' : "))
        option = random.randint(1, 2)
        print(option)
        if person_number == option:
            review_credit()
            print("ответ на Ваш запрос будет отправлен Вам на почту")
        else:
            review_credit_2()
            print("ответ на Ваш запрос будет отправлен Вам на почту")


def review_credit():
    commission = "Петрова П.П"
    f1 = open('dogovor_o_credite.txt', 'w')
    f1.write(' ***** DRD-Bank ***** \n')
    f1.write('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
    f1.write(f'| кредитный специалист: {commission} |\n')
    f1.write('----- Вам одобрено ----- \n')
    f1.write('***** Спасибо за обращение! *****\n')
    f1.close()


def review_credit_2():
    commission_2 = "Иванова И.И"
    f2 = open('dogovor_o_credite.txt', 'w')
    f2.write(' ***** DRD-Bank ***** \n')
    f2.write('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n')
    f2.write(f'| кредитный специалист: {commission_2} |\n')
    f2.write('----- Вам отказано ----- \n')
    f2.write('***** Спасибо за обращение! *****\n')
    f2.close()


def login(bank):
    while True:
        log = input("Введите ваш логин: ")
        for user in bank:
            user_s = user.split()
            if log == user_s[0]:
                time.sleep(2)
                print("** Верный логин **")
                return user_s
        time.sleep(2)
        print("-- Неверный логин --")


def payment_servise():
    option = input("Оплата:\n 1. Коммунальные платежи"
                   "\n 2. Пополнить баланс телефона"
                   "\n 3. Оплата интернета и ТВ"
                   "\n 4. Оплата штрафов ГАИ \n : ")
    if option == "1" or option == "комуналка" or option == "ком":
        print("Вы выбрали оплату коммунальных платежей")
        pl1 = input("введите адрес и номер договора: ")
    elif option == "2" or option == "на телефон" or option == "связь":
        print("Вы выбрали отлату мобильной связи ")
        pl2 = input("введите мобильного оператора: ")
        pl2_2 = input("введите номер телефона: ")
    elif option == "3" or option == "интеренет" or option == "тел":
        print("Вы выбрали оплату интернета и ТВ")
        pl3 = input("введите номер договора: ")
    elif option == "4" or option == "гаи":
        print("Вы выбрали оплату штрафов ГАИ")
        pl4 = input("введите номер протокола: ")
    else:
        print("Неверный ввод")


def new_password(user):
    while True:
        password = getpass(
            "Придумайте новый пароль: \n введите 8-ми значное число без пробелов используя большие и маленькие буквы и минимум одну цифру: \n ")
        probel = False
        b_b = False
        m_b = False
        chislo = False
        for bukva in password:
            if bukva.isupper():
                b_b = True
            if bukva.islower():
                m_b = True
            if bukva.isspace():
                probel = True
            if bukva.isdigit():
                chislo = True
        if b_b and m_b and (not probel) and chislo:
            x = []
            for elem in password:
                x.append(elem)
            myString = ''.join(x)
            user_list = start_user()
            for u_line in user_list:
                if user[0] in u_line:
                    u_line_s = u_line.split()
                    u_line_s[1] = password
                    user = u_line_s
                    user_j = ' '.join(u_line_s)
                    user_list[user_list.index(u_line)] = user_j
                    rewrite(user_list)
            time.sleep(4)
            print("Новый пароль успешно сохранен")
            time.sleep(1)
            return user
        else:
            if not b_b:
                time.sleep(1)
                print("- нет прописных букв -")
            if not m_b:
                time.sleep(1)
                print("- нет строчных букв -")
            if not chislo:
                time.sleep(1)
                print("- нет числа -")
            if probel:
                time.sleep(1)
                print("- пробелов быть не должно -")
            if len(password) > 8:
                print("- должно быть не более 8 символов -")


def payment_password(user):
    while True:
        key = getpass(
            "Введите ваш пароль: \n - Если забыли пароль нажмите 0: \n ")
        if key == "0":
            return new_password(user)
        if key == user[1]:
            time.sleep(2)
            print("** Верный пароль **")
            return user
        else:
            time.sleep(2)
            print("-- Неверный пароль -- ")
            print("*"*50)


def converter():
    dengi = float(input("Введите сумму которую нужно рассчитать: \n "))
    euro = money['euro']
    dollar = money['dollars']
    rus = money['rubl']
    while True:
        obmen = input(
            "Введите название валюты: \n 1. Евро \n 2. Доллары \n 3. Российский рубль \n 0. - для перехода в главное меню \n")
        if obmen == "0":
            break
        if obmen == "евро" or obmen == "euro" or obmen == "1":
            conv_1 = (dengi // euro)
            time.sleep(1)
            print(f"- У вас получится - {conv_1} евро")
        elif obmen == "dollar" or obmen == "доллары" or obmen == "дол" or obmen == "2":
            conv_2 = (dengi // dollar)
            time.sleep(1)
            print(f"- У вас получится - {conv_2} долларов ")
        elif obmen == "rus" or obmen == "rubl" or obmen == "рубль" or obmen == "3":
            conv_3 = (dengi * rus)
            time.sleep(1)
            print(f"- У вас получится - {conv_3} рублей ")
        else:
            time.sleep(1)
            print(" Такой валюты у нас нет")


def location():
    print(" Наш адрес : ул.Карл Маркса 1 д. 666 \n Работаем все дни кроме воскресенья с 10 до 19 \n наш тел. 888 00 234532")
    print("Все Ваши замечания и пожелания по улучшению качества услуг отправляйте нам на почту nam_vse_ravno@neotvetim.com")


def chief_bank():
    print("   ***** DRD-Bank *****")
    time.sleep(2)
    today = datetime.datetime.today()
    print(today.strftime("%Y - %m - %d"))
    print(today.strftime("Минск  - %H. %M. %S"))
    print(today.strftime("Москва - %H. %M. %S"))
    print(today.strftime("Афины  - %H. %M. %S"))
    print(today.strftime("Анкара - %H. %M. %S"))
    print("*"*50)
    time.sleep(3)
    t = True
    while t:
        choice = input(" Вас приветствует онлайн - помощник банка. Выберите или введите услугу которая Вас интересует : \n 1. Кредиты \n 2. Моя кредитная карта \n 3. Конвертер валют \n 4. Контакты / обратная связь \n 0. Закончить работу \n")
        if choice == "0":
            t = False
            print("Спасибо, что выбрали наш банк! Всего хорошего, до свидания!")
        if choice == "1" or choice == "кредиты" or choice == "кредит":
            print("---------- кредиты ----------")
            time.sleep(2)
            credit()
            print("*"*100)
        if choice == "2" or choice == "моя карта":
            print("Для работы с кредитной картой Вам необходимо авторизироваться: ")
            my_user = payment_password(login(start_user()))
            menu = input(
                "Выберите операцию :\n 1. Посмотреть баланс \n 2. Денежный перевод \n 3. Оплата услуг \n: ")
            if menu == "1":
                print(my_user)
                print(f'Ваш баланс: {my_user[2]}')
            if menu == "2" or menu == "перевод":
                print("---------- денежные переводы ----------")
                time.sleep(2)

                def co():
                    card = password.get()
                    return card

                def com():
                    pay = money.get()
                    if pay == my_user[2] or pay < my_user[2]:
                        time.sleep(4)
                        print("Операция проведена успешно")
                    else:
                        time.sleep(3)
                        print("Недостаточно средств")

                master = Tk()
                master.resizable(False, False)
                master.title("TRANSFER - MONEY")

                Label(master, text="Введите номер карты получателя: ").grid(row=1)
                Label(master, text="Введите данные получателя").grid(row=2)
                Label(master, text="Введите сумму перевода").grid(row=0)

                password = StringVar()
                money = StringVar()

                e1 = Entry(master, textvariable=money)
                e2 = Entry(master, textvariable=password, show='*')
                e3 = Entry(master)

                e1.grid(row=0, column=1)
                e2.grid(row=1, column=1)
                e3.grid(row=2, column=1)

                Label(text="Срок действия карты (год): ").grid(
                    row=2, column=2, sticky=W,
                    padx=10, pady=10)
                Spinbox(width=7, from_=2019, to=2027)\
                    .grid(row=2, column=3, padx=10)
                Label(text="Срок действия карты (месяц): ")\
                    .grid(row=1, column=2, sticky=E)
                Spinbox(width=7, from_=1, to=12)\
                    .grid(row=1, column=3, sticky=E, padx=10)

                Button(master, text='Выход', command=quit, relief=SUNKEN,
                       bd=9).grid(row=3, column=0, sticky=W, pady=4)
                Button(master, text='Перевести', command=com, relief=SUNKEN, bd=9).grid(
                    row=3, column=1, sticky=W, pady=4)
                mainloop()
                print("*"*100)

            if menu == "3" or menu == "оплата" or menu == "платеж":
                print("---------- платежи ----------")
                time.sleep(2)
                payment_servise()
                print("Введите данные карты для оплаты (8 чисел, не используйте прописные и строчные буквы, а так же другие знаки):\n ")

                def show():
                    card = password.get()
                    new_password = " "
                    shifrator = 7
                    for chislo in card:
                        new_chislo = int(chislo) + shifrator
                        new_password += str(new_chislo)
                        shifrator -= 1
                    if card.isdigit():
                        if len(card) == 8:
                            time.sleep(3)
                            print("Оплата прошла успешно")
                        else:
                            time.sleep(2)
                            print("Неправильно ввели номер карты")
                    else:
                        time.sleep(1)
                        print("Неверный символ")

                window = Tk()
                window.resizable(False, False)
                window.title("Payment window")
                window.geometry("200x100")

                password = StringVar()
                passEntry = Entry(
                    window, textvariable=password, show='*').pack()

                submit = Button(window, text='Ввести данные',
                                command=show).pack()
                submit2 = Button(window, text='Выход', command=quit).pack()
                window.mainloop()
                print("*"*100)

        if choice == "3" or choice == "конвертер":
            print("---------- конвертер валют ----------")
            time.sleep(2)
            converter()
            print("*"*100)
        if choice == "4" or choice == "контакты":
            print("---------- связь с нами ----------")
            time.sleep(2)
            location()
            time.sleep(3)
            print("*"*100)


chief_bank()
