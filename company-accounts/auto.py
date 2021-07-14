
#Авторизация или регистрация
def reg_auto():
    r_a = input("1. Авторизация\n2. Регистрация")
    if r_a.isdigit():
        r_a = int(r_a)
        if r_a == 1:
            autorization()
        elif r_a == 2:
            registration()
        else:
            print("Неправильный ввод, попробуйте ещё раз")
            reg_auto()
    else:
        print("Для ввода необходимо ввести 1 или 2, попробуйте ещё раз")
        reg_auto()

# Регистрация
def registration():
    login = input("Введите логин")
    password = input("Введите пароль")
    file1 = open("D:\python_pro\min_user.txt", "a", encoding = "utf-8")
    file1.write(login + " " + password + " " + "User")
    file1.close()
    print("Регистрация прошла успешно")

# Авторизация
def autorization():
    autorize = ""
    login = input("Введите логин")
    password = input("Введите пароль")
    file1 = open("D:\python_pro\min_user.txt", "r", encoding = "utf-8")
    for line in file1:
        line = line.split()
        if line[0] == login:
            if line[1] == password:
                if line[2] == "Admin":
                    autoriz = "Admin"
                    print("Admin")
                    return autoriz
                elif line[2] == "User":
                    autoriz = "User"
                    print("User")
                    return autorize
            else:
                print("Неправильный пароль")
                autorization()
        else:
            print("Логина не существует")
            autorization()
    file1.close()

reg_auto()



