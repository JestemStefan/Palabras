from __future__ import unicode_literals
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from random import randint


def ask(polish, spanish):

    randNum = randint(0, len(polish)-1)
    #print(randNum)
    UserInput = ""
    # for word in polish_words:

    UserInput = input("Jak jest " + polish[randNum] + " po hiszpańsku?: ")
    UserInput = UserInput.strip().replace(" ", "")
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


    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    textfile = open(filename, "r+", encoding="utf-8")

    polish_words = []
    spanish_words = []

    print("Naciśnij dowolny klawisz aby rozpocząć!")
    for line in textfile:
        langSplit = line.strip().replace(" ", "").lower().split(":")

        if len(langSplit) == 2:
            if len(langSplit[0]) and len(langSplit[1]):

                #print(len(langSplit[1]))
                polish_words.append(langSplit[0])
                spanish_words.append(langSplit[1])

    #print(polish_words)
    #print(spanish_words)

    ask(polish_words, spanish_words)

    textfile.close()


if __name__ == "__main__":
    # execute only if run as a script
    main()