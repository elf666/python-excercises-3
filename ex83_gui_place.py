# stworz okienko o rozmiarach 200x200
# uzywajac place umiesc w nim 4 przyciski, kazdy o rozmiarach 50x50
# rozmiesc je tak, aby ukladaly sie w okienku po skosie
# od lewej gory do prawego dolu
# pokoloruj kazdy na inny kolor
# dodaj do kazdedo funkcje ktora wypisuje na konsole jego kolor


from tkinter import *

def print_b1():
    print("white")

def print_b2():
    print("yellow")

def print_b3():
    print("green")

def print_b4():
    print("blue")

root = Tk()
root.geometry("200x200")

b1 = Button(bg='white', command=print_b1)
b2 = Button(bg='yellow', command=print_b2)
b3 = Button(bg='green', command=print_b3)
b4 = Button(bg='blue', command=print_b4)

b1.place(x=0, y=0, width=50, height=50)
b2.place(x=50, y=50, width=50, height=50)
b3.place(x=100, y=100, width=50, height=50)
b4.place(x=150, y=150, width=50, height=50)

root.mainloop()















# def print_button1():
#     print("white")
#
# def print_button2():
#     print("yellow")
#
# def print_button3():
#     print("green")
#
# def print_button4():
#     print("blue")
#
# from tkinter import *
#
# root = Tk()
# root.geometry("200x200")
# button1 = Button(root, text="1", bg="white", command=print_button1)
# button2 = Button(root, text="2", bg="yellow", command=print_button2)
# button3 = Button(root, text="3", bg="green", command=print_button3)
# button4 = Button(root, text="4", bg="blue", command=print_button4)
#
# button1.place(x=0, y=0, width=50, height=50)
# button2.place(x=50, y=50, width=50, height=50)
# button3.place(x=100, y=100, width=50, height=50)
# button4.place(x=150, y=150, width=50, height=50)
#
# root.mainloop()
