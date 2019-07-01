from tkinter import *

def do_some_action():
    if checkbox1.get() == True:
        button["bg"] = "red"
    else:
        button["bg"] = "lightgrey"

    if checkbox2.get() == True:
        button["fg"] = "yellow"
    else:
        button["fg"] = "black"

root = Tk()
root.title("Checkboxes")
root.geometry("250x150")

checkbox1 = BooleanVar() # klasa nalezaca do tkinter, sluzy do prezchowywania stanu przyciskow
checkbox2 = BooleanVar() # klasa nalezaca do tkinter, sluzy do prezchowywania stanu przyciskow

# mozna wyswietlic widget w tej samej linijce, w ktorej sie go tworzy
# sticky pobiera parametry W, E, S, N
Checkbutton(text="Zmien tlo na czerwony", variable = checkbox1).grid(sticky=W)
# lub przy uzyciu zmiennej
cb1 = Checkbutton(text="Zmien litery na zolty", variable = checkbox2)
cb1.grid(sticky=W)

button = Button(root, text="Action", command=do_some_action)
button.grid(sticky=N+S+W+E)

root.mainloop()

# ex85_gui_checkbox.py
