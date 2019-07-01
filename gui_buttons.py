from tkinter import *

def print1():
    print("Nacisnieto przycisk 1")
    button1.configure(bg='yellow')
    button2.configure(bg='pink')
    button2.configure(text='jestes glupi')

def print2():
    print("Nacisnieto przycisk 2")
    button2.configure(bg='white')
    button1.configure(bg='green')
    button1.configure(text='sam jestes')

root = Tk()
root.title("Buttons")
root.geometry("300x200")
button1 = Button(root, text="Przycisk 1", bg='yellow', command=print1) # dodaj funkcje do przycisku
button2 = Button(root, text="Przycisk 2",bg='white', command=print2)
# button1.pack()
# button2.pack()
button1.grid(row=0,column=0) # grid bez parametrow zachowuje sie jak pack()
button2.grid(row=1,column=1)
#
button2["bg"] = 'red' # mozna tez pozniej dodac funkcje do przycisku

root.mainloop()
