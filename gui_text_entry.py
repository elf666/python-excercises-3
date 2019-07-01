from tkinter import *

def get_entry():
    print(frame3.entry.get())

def get_text():
    print(frame4.text.get(0.0,END)) # czytaj od wiersza 0, kolumny 0, do konca

def write_entry():
    frame3.entry.delete(0, END) # usuwa elementy od 0 do konca
    frame3.entry.insert(4, "A") # od ktorego znaku zaczac pisac, co wpisac

def write_text():
    frame4.text.delete(0.0, END) # usuwa tekst od wiersza 0, kolumny 0, do konca
    frame4.text.insert(0.0, "B")

root = Tk()
root.geometry("300x300")
# Entry - jeden wiersz tekstu
# Text - blok tekstu
# oba pola można zapisywać i odczytywac
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0)

frame3.entry = Entry()
frame3.entry.grid(row=0, column=1)

frame4.text = Text(width = 30, height = 10, wrap=WORD)
frame4.text.grid(row=1, column=1)

read_entry = Button(frame1, text="Read Entry field", command=get_entry)
write_entry = Button(frame1, text="Write A to Entry", command=write_entry)
read_text = Button(frame2, text="Read Text field", command=get_text)
write_text = Button(frame2, text="Write B to Text", command=write_text)

read_entry.grid()
read_text.grid()
write_entry.grid()
write_text.grid()

root.mainloop()

# ex84_gui_get_insert.py
