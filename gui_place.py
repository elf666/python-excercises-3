# place - pozwala recznie rozmieszczac widzety z dokladnoscia do piksela

from tkinter import *

root = Tk()
root.title("Buttons")
root.geometry("300x200")


button1 = Button(root, text="Przycisk 1", bg='red')
button2 = Button(root, text="Przycisk 2", bg='blue')

button1.place(x=10, y=10, width=150)
button2.place(x=40, y=100, height = 66)

root.mainloop()

# ex83_gui_place.py
