password  = input("Введите пароль: ")

proverprobel = password.count(" ")#проверка на пробелы

abcdbolsh = password.isupper()
abcdmal = password.islower()#проверка на регистр

provercifra = password.isalpha()#проверка на цифру

cifra = password[0].isdigit()#проверка на первый введенный элемент

if proverprobel > 0 :
    print("Пароль не может содержать пробелов")
elif abcdbolsh or abcdmal == True:
    print("Пароль должен иметь буквы верхнего и нижнего регистра ")
elif provercifra == True:
    print("В пароле должна быть как минимум одна цифра")
elif cifra == True:
    print("Пароль не может начинаться с цифры")
else:
    print("Ваш пароль удволетворяет всем условиям: ",password)