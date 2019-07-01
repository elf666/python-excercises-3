# utworz okienko o tytule "9 cyfr" i wymiarach 200x150
# utworz w nim 9 buttonow o numerach od 1 - 9
# rozmiesc je przy uzyciu grid
# * dodaj 0 na srodku na dole


from tkinter import *

root = Tk()
root.title("9 cyfr")
root.geometry("200x150")

label1 = Button(root, text="1")
label2 = Button(root, text="2")
label3 = Button(root, text="3")
label4 = Button(root, text="4")
label5 = Button(root, text="5")
label6 = Button(root, text="6")
label7 = Button(root, text="7")
label8 = Button(root, text="8")
label9 = Button(root, text="9")
label0 = Button(root, text="0")
#
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=0, column=2)
label4.grid(row=1, column=0)
label5.grid(row=1, column=1)
label6.grid(row=1, column=2)
label7.grid(row=2, column=0)
label8.grid(row=2, column=1)
label9.grid(row=2, column=2)
label0.grid(row=3, column=1)

root.mainloop()
