txt = input('Введите эсэмэску: ')
txtlen = len(txt)
sms = txtlen // 60

#деление нацело, то есть без остатка
if txtlen % 60 != 0:
    sms+=1
print(f"Вы платите за {sms} эсэмэсок") 