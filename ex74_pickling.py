# stworz klase SloikOgorkow pobierajaca w konstruktorze dane:
# firma, pojemnosc, typ, cena
# stworz obiekt klasy SloikOgorkow a nastepnie przy uzyciu pickling zapisz go do pliku
# ogorek.dat
# nastepnie odczytaj obiekt ogorka z pliku i wypisz jego dane
# (te same, ktore podales w konstruktorze)

import pickle

class SloikOgorkow:

    def __init__(self, firma, pojemnosc, typ, cena):
        self.firma = firma
        self.pojemnosc = pojemnosc
        self.typ = typ
        self.cena = cena

    def __str__(self):
        return f"{self.firma}, {self.pojemnosc}, {self.typ}, {self.cena}"

sloik1 = SloikOgorkow("Rolnik", 1000, "kiszone", 10)

with open("ogorki.dat",'wb') as f:
    pickle.dump(sloik1, f)

with open("ogorki.dat", 'rb') as f:
    print(pickle.load(f))









# import pickle
#
# class SloikOgorkow:
#
#     def __init__(self, firma, pojemnosc, typ, cena):
#         self.firma = firma
#         self.pojemnosc = pojemnosc
#         self.typ = typ
#         self.cena = cena
#
# sloik1 = SloikOgorkow("Rolnik", "800ml", "kiszone", 10)
#
# with open("ogorek.dat", "wb") as f1:
#     pickle.dump(sloik1, f1)
#
# with open("ogorek.dat", "rb") as f2:
#     ogorek = pickle.load(f2)
#
# print(ogorek.firma, ogorek.pojemnosc, ogorek.typ, ogorek.cena)
