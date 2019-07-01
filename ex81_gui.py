# przy uzyciu tkinter stworz okienko o wymiarach 300x200 pikseli
# i tytule: "Exercise 1 - Labels"
# umiesc w nim cztery etykiety: lewa_gora, prawa_gora, lewy_dol, prawy_dol
# rozmiesc je w miejscach odpowiadajacych ich nazwie




from tkinter import *

root = Tk()
root.title("Exercise 1 - Labels")
root.geometry("300x200")

frame_l = Frame(root)
frame_r = Frame(root)

frame_l.pack(side=LEFT)
frame_r.pack(side=RIGHT)

lewa_gora = Label(frame_l, text="Lewa gora")
lewy_dol = Label(frame_l, text="Lewy dol")
prawa_gora = Label(frame_r, text="Prawa gora")
prawy_dol = Label(frame_r, text="Prawy dol")

lewa_gora.pack(side=TOP)
lewy_dol.pack(side=BOTTOM)
prawa_gora.pack()
prawy_dol.pack()

root.mainloop()










# from tkinter import *
#
# root = Tk()
# root.title("Exercise1 - Labels")
# root.geometry("300x200")
# frame1 = Frame(root)
# frame2 = Frame(root)
# frame1.pack(side = LEFT)
# frame2.pack(side = RIGHT)
#
# lewa_gora = Label(frame1, text="Lewa gora")
# lewy_dol = Label(frame1, text="Lewy dol")
# prawa_gora = Label(frame2, text="Prawa gora")
# prawy_dol = Label(frame2, text="Prawy dol")
# lewa_gora.pack(side = TOP)
# lewy_dol.pack(side = BOTTOM)
# prawa_gora.pack(side = TOP)
# prawy_dol.pack(side = BOTTOM)
#
#
# root.mainloop()
