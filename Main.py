from __future__ import unicode_literals
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from random import randint
from tkinter import *

polish_words = []
spanish_words = []

w = ["uno", "dos", "tres", "quadro", "sinko"]



def make_tables(root, word):
    entries = []
    i = 0

    for w in word:
        Label(root, text=w, width=15, anchor='w').grid(row=i)
        ent = Entry(root)
        ent.grid(row=i, column=1)
        entries.append(ent)
        i += 1
    return entries


def fetch(entries):
    print(entries[0].get())
    for entry in entries:
        text = entry.get()
        print('%s' % text)

def get_words():
    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename(title="Wybierz plik ze słówkami",
                               filetypes=(("Plik tekstowy", "*.txt"), ("Wszystkie pliki", "*.*")))

    textfile = open(filename, "r+", encoding="utf-8")

    print("Hiszpańskie litery: á, é, í, ó, ú, ü, ñ, ¿, ¡ \n")
    # print("Naciśnij dowolny klawisz aby rozpocząć!")
    for line in textfile:
        langSplit = line.strip().replace("  ", " ").lower().split(":")

        if len(langSplit) == 2:
            if len(langSplit[1]) and len(langSplit[0]):
                polish_words.append(langSplit[1])
                spanish_words.append(langSplit[0])

    # print(polish_words)
    # print(spanish_words)
    textfile.close()


def ask(polish, spanish):

    randNum = randint(0, len(polish)-1)
    #print(randNum)
    UserInput = ""
    # for word in polish_words:

    UserInput = input("Jak jest " + polish[randNum] + " po hiszpańsku?: ")
    UserInput = UserInput.strip().replace("  ", " ")
    UserInput = UserInput.lower()
    #print(UserInput)

    if UserInput == spanish[randNum]:
        print("Muy bien!")
    else:
        print("Fatal! Prawidłowa odpowiedź to " + spanish[randNum])

    polish.pop(randNum)
    spanish.pop(randNum)
    if len(polish) > 0:
        ask(polish, spanish)
    else:
        print("Nie ma więcej słówkek!")
        input("")

def main():


    root = Tk()

    ents = make_tables(root, w)

    print(ents)

    b1 = Button(root, text='Show',command=(lambda e=ents: fetch(e))).grid(row=6, column=1)

    root.mainloop()

    if len(polish_words) > 0 and len(spanish_words) > 0:
        ask(polish_words, spanish_words)
    else:
        print("Brak słówek, Wybierz odpowiedni plik txt!")




#if __name__ == "__main__":
    #main()



main()