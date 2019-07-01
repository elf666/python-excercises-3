from tkinter import *

root = Tk()
root.title("Grids")
root.geometry("300x200")

lewa_gora = Button(root, text="Lewa gora")
lewy_dol = Button(root, text="Lewy dol")
prawa_gora = Button(root, text="Prawa gora")
prawy_dol = Button(root, text="Prawy dol")
lewa_gora.grid(row=0, column=0) # podajemy w ktorzym rzedzie i ktorej kolumnie
lewy_dol.grid(row=1, column=0)  # ma znajdowac sie widget
prawa_gora.grid(row=0, column=1)
prawy_dol.grid(row=1, column=1)


root.mainloop()

# ex82_gui_grid.py
