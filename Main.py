from __future__ import unicode_literals
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from random import randint


def ask(polish, spanish):

    randNum = randint(0, len(polish)-1)
    #print(randNum)
    UserInput = ""
    # for word in polish_words:

    UserInput = input("Jak jest " + polish_words[randNum] + " po hiszpańsku?: ")
    UserInput.strip().replace(" ", "")
    UserInput = UserInput.lower()
    #print(UserInput)

    if UserInput == spanish_words[randNum]:
        print("Muy bien!")
    else:
        print("Fatal! Prawidłowa odpowiedź to " + spanish_words[randNum])

    polish.pop(randNum)
    spanish.pop(randNum)
    if len(polish) > 0:
        ask(polish, spanish)
    else:
        print("Nie ma więcej słówkek!")
        input("")



Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

textfile = open(filename, "r+", encoding="utf-8")

polish_words = []
spanish_words = []

for line in textfile:
    langSplit = line.strip().replace(" ", "").lower().split(":")
    #print(langSplit)
    #print(langSplit)
    polish_words.append(langSplit[0])
    spanish_words.append(langSplit[1])

#print(polish_words)
#print(spanish_words)

ask(polish_words, spanish_words)

textfile.close()


