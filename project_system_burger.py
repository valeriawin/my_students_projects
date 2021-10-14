goods = {
    "bread":   {"price": 1,  "number": 10},
    "chees":    {"price": 2,  "number": 10},
    "rostbif": {"price": 3,  "number": 10}
    }


def new_good():
    product = input("введи товар ")
    if product in goods:
        print("Продукт", product, "имеется в программе ", goods[product])
    else:
        goods[product] = input("такого товара нет в программе, Введи наименование товар заново, чтобы добавить в программу ")
        goods[product]= {"price":0,  "number":0}
        goods[product]["number"] = int(input("введите количество "))
        goods[product]["price"] = int(input("введите цену "))

    
def price_bread():
    price_bread = 0
    if goods["bread"]["number"] > 0:
        for i in goods:
            if i == "bread":
                price_bread += goods["bread"]["price"]
                return int(price_bread)
    else:
        return 0 


def price_chees():
    price_chees = 0   
    if goods["chees"]["number"] > 0:
        for i in goods:
            if i == "chees":
                price_chees += goods["chees"]["price"]
                return int(price_chees)
    else:
        return 0


def price_rostbif():
    price_rostbif = 0
    if goods["rostbif"]["number"] > 0:
        for i in goods:
            if i == "rostbif":
                price_rostbif += goods["rostbif"]["price"]
                return int(price_rostbif)
    else:
        return 0


def price_burger():
    if price_bread and price_chees and price_rostbif != 0:
        return price_bread() + price_chees() + price_rostbif()
    else:
        print ("проверьте остаток на складе")


def good_is():
    goods["chees"]["number"] = goods["chees"]["number"]-a
    goods["bread"]["number"] = goods["bread"]["number"]-a
    goods["rostbif"]["number"] = goods["rostbif"]["number"]-a     
    print(f"Товары на складе: {goods}") 
 

def not_enough():
    if goods["chees"]["number"] <=0 or goods["bread"]["number"]<=0 or goods["rostbif"]["number"]<=0:
        print("недостаточно продуктов на складе")


b = int(input("Если хотите добавить товар введите 1, если нет = 0 "))

while b == 1:
    new_good()
    b = int(input("Если хотите доавить товар введите 1, если нет = 0 "))
    
a = int(input("введите количество бургеров, которых необходимо произвести "))

while a !=0:
    price_bread()
    price_chees()
    price_rostbif()
    price_burger()
    print(f"Себестоимость бургера {price_burger()} рублей")
    print(f"Себестоимость {a} бургеров: {price_burger()*a}  рублей")
    good_is()
    not_enough()
    
    a = int(input("введите количество бургеров, которых необходимо произвести или - 0, чтобы выйти "))
    
  



 



