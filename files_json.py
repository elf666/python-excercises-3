# JSON - JavaScript Object Notation
# uzywany nie tylko w javascripcie
# z punktu widzenia Pythona json wyglada jak lista zagniezdzonych slownikow
# https://pl.wikipedia.org/wiki/JSON
# biblioteka do obslugi json dziala bardzo podobnie do pickle

import json

slownik1 = {'janek': 35, 'marek': 30, 'jozek': 25}
slownik2 = {'header':'TITLE', 'body': {"line1": "data1", "line2": "data2"}, "footer":"bye!"}

with open("json_data.json", "w") as f: # podajemy "w" a nie "wb" jak w pickle
    json.dump(slownik2, f)

with open("json_data.json", "r") as f: # podajemy "r" a nie "rb" jak w pickle
    D = json.load(f)
    print(D.keys())

# ex80_json.py
