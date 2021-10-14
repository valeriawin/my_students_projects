def rewrite(bank):
    f = open("user.txt", "w")

    for elem in bank:
        if elem[-1] != "\n":
            elem = elem + "\n"

        f.write(elem)
        
    f.close()


def start_user():
    file1 = open("user.txt", "r")
    bank = []

    for line in file1:
        bank.append(line)

    file1.close()

    return bank


def add_user(bank):
    print(bank)

    while True:
        temp = input('введите карту или 0 для выхода: ')
        if temp == "0":
            break
        else:
            bank.append(temp)

    rewrite(bank)


def delete_user(bank):
    print(bank)

    while True:
        temp = input('введите карту, которую хотите удалить, или 0 для выхода: ')
        if temp == "0":
            break
        else:
            for elem in bank:
                if elem[:len(elem)-1] == temp:
                    bank.remove(elem)

    rewrite(bank)
