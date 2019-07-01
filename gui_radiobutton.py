from tkinter import *

def do_some_action():
    if choosen.get() == 'czerwony':
        button["background"] = 'red'
    else:
        button["background"] = 'yellow'

root = Tk()
root.title("Radiobuttons")
root.geometry("250x150")

choosen = StringVar() # klasa nalezaca do tkinker, sluzy do prezchowywania stanu przyciskow
choosen.set(None) # ustawianie poczatkowej wartosci, zaden z radiobuttonow nie jest wybrany

Radiobutton(text="Zmien tlo na czerwony", variable = choosen, value='czerwony').grid(sticky=W)
Radiobutton(text="Zmien tlo na zolty", variable = choosen, value='zolty').grid(sticky=W)

button = Button(root, text="Action", command=do_some_action)
button.grid(sticky=N+S+W+E)


root.mainloop()

# ex86_gui_radio.py
