# stworz program okienkowy bedacy kalkulatorem BMI
# musi posiadac pole do pobierania wzrostu i pole do pobierania wagi
# przycisk "Oblicz" oraz pole do wypisywania wyniku
# nadaj odpowiednie labelki
# BMI = waga / wzrost_wyrazony_w_metrach ** 2


from tkinter import *

def oblicz_bmi():
    waga = float(frame_waga.entry.get())
    wzrost = float(frame_wzrost.entry.get()) / 100
    bmi = round(waga / (wzrost ** 2),2)
    frame_wynik.entry.delete(0, END)
    frame_wynik.entry.insert(0, bmi)

root = Tk()
root.title("BMI calculator")
root.geometry("250x150")

waga_label = Label(root, text="Podaj wage w kg")
wzrost_label = Label(root, text="Podaj wzrost w cm")
oblicz_button = Button(root, text="Oblicz", command=oblicz_bmi)
wynik_label = Label(root, text="Twoje BMI wynosi")

waga_label.grid(row=0, column=0)
wzrost_label.grid(row=1, column=0)
oblicz_button.grid(row=2, column=0)
wynik_label.grid(row=3, column=0)

frame_waga = Frame(root)
frame_waga.entry = Entry()
frame_waga.entry.grid(row=0, column=1)

frame_wzrost = Frame(root)
frame_wzrost.entry = Entry()
frame_wzrost.entry.grid(row=1, column=1)

frame_wynik = Frame(root)
frame_wynik.entry = Entry()
frame_wynik.entry.grid(row=3, column=1)

root.mainloop()
