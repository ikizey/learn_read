from tkinter import *

window = Tk()

window.title = ("Читайка")
window.geometry('300x200')
btn = Button(window, text="мама", font=("Arial Bold", 50))
btn.grid(column=0, row=0)

btn = Button(window, text="папа", font=("Arial Bold", 50))
btn.grid(column=2, row=0)


window.mainloop()
