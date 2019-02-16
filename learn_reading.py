from tkinter import *
from random import shuffle

window = Tk()

window.title = ("Читайка")
window.geometry('550x300')

l = ["мама", "папа", "молоко",
     "мы", "вы", "ты",
     "каша", "вода", "море",
     "стол", "стул", "мыло"]

shuffle(l)
d = {}
buttons = []
r, c = 0, 0
for i, word in enumerate(l):
    d[i] = word
    if i % 3 == 0:
        c = 0
        r += 1
    else:
        c += 1
    print(i, i%3, c, r)
    buttons.append(Button(window, text=word, font=("Arial Bold", 50)))
    buttons[i].grid(column=c, row=r)


window.mainloop()
