from __future__ import unicode_literals
from tkinter.filedialog import askopenfilename
from random import randint
from tkinter import *

words = []
wordsLoaded = False
tableDone = False

def make_tables(root, word):
    entries = []
    i = 0

    for w in word:
        Label(root, text=w, width=15, anchor='center').grid(row=i)
        ent = Entry(root)
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries.append(ent)
        i += 1
    return entries


def check_words(entries):
    for entry in entries:
        text = entry.get()
        if text == "word":
            entry.configure({"background": "#caffab"})
        else:
            entry.configure({"background": "#ffbaab"})
        #print('%s' % text)


def get_words(button, root):

    global words
    global wordsLoaded

    polish_words = []
    spanish_words = []

    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename(title="Wybierz plik ze słówkami",
                               filetypes=(("Plik tekstowy", "*.txt"), ("Wszystkie pliki", "*.*")))
    Tk().destroy()
    textfile = open(filename, "r+", encoding="utf-8")

    print("Hiszpańskie litery: á, é, í, ó, ú, ü, ñ, ¿, ¡ \n")
    # print("Naciśnij dowolny klawisz aby rozpocząć!")
    for line in textfile:
        langSplit = line.strip().replace("  ", " ").lower().split(":")

        if len(langSplit) == 2:
            if len(langSplit[1]) and len(langSplit[0]):
                polish_words.append(langSplit[1])
                spanish_words.append(langSplit[0])

    textfile.close()

    if len(polish_words) > 0 and len(spanish_words) > 0:
        words = [spanish_words, polish_words]
        wordsLoaded = True

        ents = make_tables(root, words[1])
        b2 = Button(root, text='Sprawdź!', command=(lambda e=ents: check_words(e))).grid(row=len(words[1]), column=1)

        root.geometry("300x750")

    else:
        print("Brak słówek, Wybierz odpowiedni plik txt!")

    button.destroy()


def ask(polish, spanish):

    randNum = randint(0, len(polish)-1)

    UserInput = input("Jak jest " + polish[randNum] + " po hiszpańsku?: ")
    UserInput = UserInput.strip().replace("  ", " ")
    UserInput = UserInput.lower()

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

def quit(r):
    r.destroy()

def main():

    root = Tk()
    root.title("Palabras")

    b1 = Button(root, text='Wybierz słówka', command=lambda: get_words(b1, root))
    b1.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.wm_protocol("WM_DELETE_WINDOW", lambda arg=root: quit(arg))

    root.mainloop()


main()