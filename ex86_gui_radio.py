# przerob program do obliczania BMI dodajac trzy radiobuttony:
# "Mow prawde", "Zanizaj o 5", "Podnos o 5"
# modyfikuj wynik w zaleznosci od tego, ktory radibutton jest wybrany
# defaultowo ustaw "mow prawde"










from tkinter import *

def oblicz_bmi():
    waga = int(frame_waga.entry.get())
    wzrost = int(frame_wzrost.entry.get()) / 100
    bmi = round(waga / (wzrost ** 2),2)

    if choosen.get() == 'zanizaj':
        bmi -= 5
    elif choosen.get() == 'podnos':
        bmi += 5

    frame_wynik.entry.delete(0, END)
    frame_wynik.entry.insert(0,bmi)


root = Tk()
root.title("BMI calculator")
root.geometry("250x200")

waga_label = Label(root, text="Podaj wage w kg")
wzrost_label = Label(root, text="Podaj wzrost w cm")
oblicz_button = Button(root, text="Oblicz", command=oblicz_bmi)
wynik_label = Label(root, text="Twoje BMI wynosi")

frame_waga = Frame(root)
frame_waga.entry = Entry()
frame_waga.entry.grid(row=0, column=1)

frame_wzrost = Frame(root)
frame_wzrost.entry = Entry()
frame_wzrost.entry.grid(row=1, column=1)

frame_wynik = Frame(root)
frame_wynik.entry = Entry()
frame_wynik.entry.grid(row=3, column=1)


waga_label.grid(row=0, column=0)
wzrost_label.grid(row=1, column=0)
oblicz_button.grid(row=2, column=0)
wynik_label.grid(row=3, column=0)

choosen = StringVar()
choosen.set('prawda')

Radiobutton(text="Mow prawde", variable = choosen, value='prawda').grid(sticky=W)
Radiobutton(text="Zanizaj o 5", variable = choosen, value='zanizaj').grid(sticky=W)
Radiobutton(text="Podnos o 5", variable = choosen, value='podnos').grid(sticky=W)

root.mainloop()
