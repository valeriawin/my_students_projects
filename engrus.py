from tkinter import *
import random

# все слова, которые знает программа
words = {'YEAR': 'ГОД', 'FIRE': 'ОГОНЬ'}
rus_words = words
eng_words = dict([[v, k] for k, v in words.items()])

cnt = 0

# отобразить главное меню
def showMenu():
    menu1.pack()
    menu2.pack()

# скрыть главное меню
def hideMenu():
    menu1.pack_forget()
    menu2.pack_forget()

# случайный выбор слова
def chooseWord(language):
    if language == "rus":
        return random.choice([i for i in rus_words])
    elif language == "eng":
        return random.choice([i for i in eng_words])

# главная функция
def startLevel(lang):
    hideMenu()
    word = chooseWord(lang)

    # добавление случайных букв
    if lang == "rus":
        label1 = Label(root, text=rus_words.get(word), font="Arial 20")
        randomLetters = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                         for i in range(25 - len(word))]
    elif lang == "eng":
        label1 = Label(root, text=eng_words.get(word), font="Arial 20")
        randomLetters = [random.choice(
            'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ') for i in range(25 - len(word))]

    label1.grid(columnspan=5, sticky="ew")

    letters = [i for i in word]
    letters += randomLetters

    random.shuffle(letters)

    buttons = []
    column = 0
    row = 3

    # создание кнопок для букв
    for i in range(0, len(letters)):
        buttons.append(Button(root, text=letters[i], width=5))
        buttons[i].config(command=lambda button=buttons[i]: chooseLetter(button))
        buttons[i].grid(column=column, row=row, sticky="ew")

        column += 1
        if column > 4:
            column = 0
            row += 1

    label2 = Label(root, text="", font="Arial 20")

    label2.grid(columnspan=5, sticky="ewsn")

    # обрабатывает правильные и неправильные буквы
    def chooseLetter(button):
        global cnt
        if button.cget("text") == word[cnt] and button.cget("bg") != "green":
            button.config(bg="green")
            label2.config(text=label2.cget("text") + word[cnt])
            cnt += 1
        elif button.cget("bg") != "green":
            for i in buttons:
                i.config(bg="SystemButtonFace")
            label2.config(text="")
            cnt = 0
        if cnt > len(word) - 1:
            cnt = 0
            delete()
            showMenu()

    # очистка уровня
    def delete():
        del letters[:]
        for i in buttons:
            i.destroy()
        del buttons[:]
        label1.destroy()
        label2.destroy()


# свойства окошка
root = Tk()
root.resizable(width=False, height=False)
root.title("Learning English")
root.geometry("225x230")

menu1 = Button(root, text="Can you translate?\nENG->RUS", width=300,
               height=7, command=lambda lang="eng": startLevel(lang))
menu2 = Button(root, text="Can you translate?\nRUS->ENG", width=300,
               height=7, command=lambda lang="rus": startLevel(lang))

showMenu()

# не забывать писать в конце!
root.mainloop()
