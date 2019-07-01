# stworz plik json zawierajacy baze danych zamowien
# kazde zamowienie posiada id, liste produktow (slownik), klienta
# lista produktow to slownik {produkt:[ilosc, cena]}
# stworz trzy rozne zamowienia#
# przeczytaj plik bazy danych zamowien i na podstawie uzyskanych danych
# oblicz sumaryczna wartosc wszystkich trzech zamowien
import json

with open("order.json", 'r') as f:
    orders = json.load(f) #orders jest slownikiem

total_ordres_value = 0
for order in orders:
    quantity = orders[order]['produkty'][1]
    value = orders[order]['produkty'][2]
    total_ordres_value += quantity * value

print(f"Total value of all orders: {total_ordres_value}.")
