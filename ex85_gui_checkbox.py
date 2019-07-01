# stworz GUI z trzema polami Entry, opisz je A, B i Suma
# stworz dwa checkboxy opisane 'dodaj tekst z A' i 'dodaj tekst z B'
# stworz kod, ktory spowoduje, ze w polu Suma pojawi sie:
# tylko tekst z A, jesli zaznaczony jest checkbox A
# tylko tekst z B, jesli zaznaczony jet checkbox B
# suma tekstu z obu checkboxkow jesli zaznaczone sa oba











from tkinter import *

def sum_text():
    result = ''
    if checkbox_a.get() == True:
        result += frame1.entry.get()
    if checkbox_b.get() == True:
        result += frame2.entry.get()
    frame3.entry.delete(0, END)
    frame3.entry.insert(0, result)


root = Tk()
root.title("Checkboxes Ex")
root.geometry("250x150")

label_a = Label(root, text="A:")
label_b = Label(root, text="B:")
label_sum = Label(root, text="Sum:")
label_a.grid(row=0, column=0, sticky=E)
label_b.grid(row=1, column=0, sticky=E)
label_sum.grid(row=2, column=0, sticky=E)

frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)

frame1.entry = Entry()
frame1.entry.grid(row=0, column=1)

frame2.entry = Entry()
frame2.entry.grid(row=1, column=1)

frame3.entry = Entry()
frame3.entry.grid(row=2, column=1)

checkbox_a = BooleanVar()
checkbox_b = BooleanVar()

Checkbutton(text="Dodaj tekst z A", variable = checkbox_a).grid(sticky=W)
Checkbutton(text="Dodaj tekst z B", variable = checkbox_b).grid(sticky=W)

button = Button(root, text="Sumuj", command=sum_text)
button.grid()

root.mainloop()

# ex85_gui_checkbox.py
