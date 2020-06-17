from __future__ import unicode_literals
from tkinter.filedialog import askopenfilename
from tkinter import *
import random as rng

words = []
entries = []
filename = ""


def get_words(button, root, file):

    global words
    global filename

    polish_words = []
    spanish_words = []
    if filename == "":
        filename = askopenfilename(title="Wybierz plik ze słówkami",
                                   filetypes=(("Plik tekstowy", "*.txt"), ("Wszystkie pliki", "*.*")))
    else:
        if file == "":
            # show an "Open" dialog box and return the path to the selected file
            filename = askopenfilename(title="Wybierz plik ze słówkami",
                                       filetypes=(("Plik tekstowy", "*.txt"), ("Wszystkie pliki", "*.*")))
        else:
            filename = file

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

        # randomize words
        z = list(zip(spanish_words, polish_words))
        rng.shuffle(z)
        z = z[:20]
        print(z)

        spanish_words[:], polish_words[:] = zip(*z)

        words = [spanish_words, polish_words]

        tables = make_tables(root, words[1])

        ents = tables[0]
        labels = tables[1]

        selectFileButton = Button(root, text='Wybierz plik', command=(lambda: new_file(root)))
        selectFileButton.configure({"font": "Calibri 14 normal"})
        selectFileButton.grid(row=len(words[1]), column=0)

        newWordsButton = Button(root, text='Losuj słówka', command=(lambda: new_words(root)))
        newWordsButton.configure({"font": "Calibri 14 normal"})
        newWordsButton.grid(row=len(words[1]), column=1)


        checkButton = Button(root, text='Sprawdź!', command=(lambda e=ents: check_words(e, root, words[0])))
        checkButton.configure({"font": "Calibri 14 normal"})
        checkButton.grid(row=len(words[1]), column=2, padx=20, pady=20)

        root.geometry("")

    else:
        print("Brak słówek, Wybierz odpowiedni plik txt!")

    button.destroy()



def make_tables(root, word):
    entries = []
    labels = []
    i = 0

    for w in word:
        lab = Label(root, text=w, width=len(w), anchor='center')
        lab.configure({"font": "Calibri 14 normal"})
        lab.grid(row=i, padx=5, pady=5)
        labels.append(lab)

        ent = Entry(root, justify='center')
        ent.configure({"font": "Calibri 14 normal"})
        ent.grid(row=i, column=1, padx=5, pady=5)
        entries.append(ent)
        i += 1

    tables = [entries, labels]
    return tables


def check_words(entries, root, spanish_words):

    # find longest word to resize Label
    longest_word = max(spanish_words, key=len)

    for i, entry in enumerate(entries):
        text = entry.get()

        text = text.strip().replace("  ", " ")
        text = text.lower()
        if text == spanish_words[i]:
            # if answer is correct then make entry box green
            entry.configure({"background": "#caffab", "font": "Calibri 14 normal"})
            l = Label(root, text="Muy bien! :)", width=len(longest_word), anchor='center', bg="#caffab")
            l.configure({"font": "Calibri 14 normal"})
            l.grid(column=2, row=i)

        # if answer is wrong or there is no answer then make entry box red
        elif text == "":
            entry.configure({"background": "#ffbaab", "font": "Calibri 14 normal"})
            l = Label(root, text=spanish_words[i], width=len(longest_word), anchor='center', bg="#fcffad")
            l.configure({"font": "Calibri 14 normal"})
            l.grid(column=2, row=i)

        # overstrike wrong answer
        else:
            entry.configure({"background": "#ffbaab", "font": "Calibri 14 overstrike"})
            l = Label(root, text=spanish_words[i], width=len(longest_word), anchor='center', bg="#fcffad")
            l.configure({"font": "Calibri 14 normal"})
            l.grid(column=2, row=i)

        # clear user input
        entry.delete(0, END)
        entry.insert(0, text)

        root.geometry("")


def new_file(root):

    new_file = askopenfilename(title="Wybierz plik ze słówkami",
                                   filetypes=(("Plik tekstowy", "*.txt"), ("Wszystkie pliki", "*.*")))
    if new_file !="":

        for widget in root.winfo_children():
            widget.destroy()

        temp_button = Button(root)
        get_words(temp_button, root, new_file)
    else:
        return None


def new_words(root):
    global filename

    for widget in root.winfo_children():
        widget.destroy()

    temp_button = Button(root)
    get_words(temp_button, root, filename)

def quit(r):
    r.destroy()

def main():

    root = Tk()
    root.title("Palabras")

    b1 = Button(root, text='Wybierz słówka', command=lambda: get_words(b1, root, ""))
    b1.configure({"font": "Calibri 14 normal"})
    b1.place(relx=0.5, rely=0.5, anchor=CENTER)

    root.wm_protocol("WM_DELETE_WINDOW", lambda arg=root: quit(arg))

    root.mainloop()


main()