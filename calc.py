# Усложни свой калькулятор. Добавь в него:
# расчёт факториала
# возведение в степень
# модуль
# логарифм (основание тоже вводится)
# рассчет процентного соотношения. 

# *В этой программе должны быть использованы принятие аргумента, рекурсия и возврат значения. 
import math

# факториал
def fact(pervoe):             
    if pervoe == 0: 
        return 1
    else:
        return pervoe * fact(pervoe-1)

# степень
def vozvedenie(pervoe,vtoroe):
    vozved = 1
    for i in range(vtoroe):
        vozved = vozved*pervoe
    return vozved

# модуль
def modyl(pervoe):
    if pervoe < 0:
        return pervoe*(-1)

#math.log(X, [base]) - логарифм X по основанию base. Если base не указан, вычисляется натуральный логарифм.

# логарифм
def logarifm(pervoe,vtoroe):
    return math.log(pervoe,vtoroe)
    
# процент
def procent(pervoe,vtoroe):
    return pervoe/vtoroe * 100
    
###########################################################

pervoe = int(input("Введите первое число: ")) # первое число
oper = input("Выберите операция +,-,*,/: ") # знак операции
if oper =="!":
    print(fact(pervoe))
elif oper =="||":
    print(modyl(pervoe))
else:
    vtoroe = int(input("Введите второе число: ")) # второе число для оставшихся операций
    if oper == '+':
        oper = pervoe + vtoroe
        print(oper, "Результат суммы чисел")
    elif oper == '-':
        oper = pervoe - vtoroe
        print(oper, "Результат разности чисел")
    elif oper == '*':
        oper = pervoe * vtoroe
        print(oper, "Результат умножения чисел")
    elif oper == '/':  
        if pervoe == 0 or vtoroe == 0:
            print("Делить на ноль нельзя")     
        else:
            oper = pervoe / vtoroe
            print(oper, "Результат деления чисел")
    elif oper == "^":
        print(vozvedenie(pervoe,vtoroe))
    elif oper == "log":
        print(logarifm(pervoe,vtoroe))
    elif oper == "%":
        print(procent(pervoe,vtoroe))