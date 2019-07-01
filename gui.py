from tkinter import *

# Tworzenie najbardziej podstawowego okna
root = Tk() # tylko jeden root na program!
# root.mainloop() # glowna petla zarzadzaja wykonaniem programu

# Dodanie tytulu i wymiarow
root.title("Moje nowe super okno")
root.geometry("400x250") # rozmiar podajemy jako string, w pikselach, szer x wys
# #
# # Widzety - obiekty w oknie
# # tworzac widzet przekazuje do jego konstruktora obiekt nadrzedny
frame1 = Frame(root)
frame2 = Frame(root)
# # pack - jedna z metod rozmieszczania/wyswietlenia obiektow, side = STRONA
frame1.pack(side = TOP) # inne: LEFT, RIGHT, TOP i BOTTOM
frame2.pack(side = BOTTOM)
# #
label1 = Label(frame1, text="Etykietka 1", background = 'red', fg="white") #fg - kolor tekstu
label2 = Label(frame2, text="Etykietka 2", bg = 'yellow') # bg = background
label3 = Label(frame2, text="Etykietka 3", bg = '#63A616')
label1.pack()
label2.pack(side=LEFT)
label3.pack()
# #
# # # Glowna petla obslugujaca program
root.mainloop()

# # ex81_gui.py
