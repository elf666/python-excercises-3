# wpisywanie danych do pliku

# with open("new_file.txt", "w") as f:
#     f.write("dzien dobry\n")
#
# with open("new_file.txt", "w") as f: # ponowne stworzenie pliku spowoduje jego nadpisanie
#     f.write("do widzenia\n")
#
# with open("new_file.txt", "a") as f: # a - dodaje dane na koncu pliku
#     f.write("cos nowego\n")           # jesli plik nie istnieje to go tworzy
#     f.write("jeszcze cos")
#     f.write("xxxyyyzzz")

 # jesli chcemy znak nowej linii na koncu linijki, to musimy go dodac: "\n"

 # ex72_write.py

 # mozemy wpisywac do pliku liste stringow przy uzyciu metody .writelines()

L = ['ala\n', 'ma\n', 'jenota\n']

with open("jenot.txt","w") as file:
    file.writelines(L)

# ex73_write.py
