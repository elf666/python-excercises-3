# zapisywanie do pliku zlozonych struktur danych (listy, slowniki)
# pickling - konserwowanie

import pickle

names = ['Janina', 'Tadeusz', 'Zbigniew']
numbers = (1,2,4,6,8,10)
some_dict = {'abc': "ABC", 'def': "DEF"}

with open("data.dat","wb") as f1: # plik nie musi miec rozszerzenia .txt, bardziej pasuje .dat
    pickle.dump(names, f1)         # aby zapisac musimy podac tryb wb - write binary
    pickle.dump(numbers, f1)       # oraz podac strukture danych i obiekt pliku
    pickle.dump(some_dict, f1)

with open("data.dat", "rb") as f:     # aby odczytac podajemy tryb rb - read binary
    a = pickle.load(f)  # podac do jakiej zmiennej czytamy i z jakiego pliku
    b = pickle.load(f)
    c = pickle.load(f)

    print(a,b,c)

# ex74_pickling.py
