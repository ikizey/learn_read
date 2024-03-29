from random import shuffle
from tkinter import *
from playsound import playsound # i don't like this one.

window = Tk()
window.title = ("LearnRead")
window.configure(background='green')
w = 1250
h = 720
ws = window.winfo_screenwidth() # width of the screen
hs = window.winfo_screenheight() # height of the screen
# calculate x and y coordinates for the Tk root window
x = int((ws/2) - (w/2))
y = int((hs/2) - (h/2))
window.geometry(f"{w}x{h}+{x}+{y}")

# word list
# playsound can't open files with cyrillic letters in it's name, so i have to
# add mapping to "translit" words. Otherwise just russian words would be on list
l = [("мама", "mama"), ("папа", "papa"), ("молоко", "moloko"),
     ("мы", "my"), ("вы", "vy"), ("ты", "ty"),
     ("каша", "kasha"), ("вода", "voda"), ("море", "more"),
     ("стол", "stol"), ("стул", "stul"), ("мыло", "mylo"),
     ("хлеб", "hleb"), ("яблоко", "yabloko"), ("дом", "dom"),
     ("суп", "sup"), ("обед", "obed"), ("игрушка", "igrushka"),
     ("рот", "rot"), ("нос", "nos"), ("ухо", "uho"),
     ("сон", "son"), ("телефон", "telefon"), ("чай", "chai"),
     ("кофе", "kofe"), ("собака", "sobaka"), ("бегать", "begat"),
     ("еда", "eda"), ("сыр", "syr"), ("корова", "korova"),
     ("мышь", "mysh"), ("чайник", "chainik"), ("котлета", "kotleta"),
     ("зуб", "zub"), ("круг", "krug"), ("день", "den"),
     ("сегодня", "segodnya"), ("фигура", "figura"), ("много", "mnogo"),
     ("поезд", "poezd"), ("магазин", "magazin"),
     ("кот", "kot"), ("дети", "deti"), ("машина", "mashina")]

shuffle(l)

# returns argumentless function. for assigning it to button press event command=
def play_mp3(mp3):
    def x():
        playsound(mp3)
    return x

#amount of columns in button
columns = 4

buttons = []
r, c = 0, 0
# run through shuffled list, making buttons, assigning functions to them
# and adding them to grid.
for i, word in enumerate(l):
    if i % columns == 0:
        c = 0
        r += 1
    else:
        c += 1
    ps = play_mp3(f"sounds/{word[1]}.mp3")
    buttons.append(Button(window, text=f"{i+1}.{word[0]}"
                          , font=("Arial Bold", 50), command=ps))
    buttons[i].grid(column=c, row=r)


window.mainloop()
