# __name__ - specjalna zmienna, ktora wyswietla nazwe danego modulu
# jesli modul zostal uruchomiony bezposrednio, wtedy __name__ == '__main__'
# jesli modul zostal zaimportowany wtedy pod __name__ kryje sie jego nazwa

# print(__name__)

import module1

# sprawdzenie if __name__ == '__main__' pozwala nam wydzielic blok kodu,
# ktory będzie się wykonywał tylko przy bezposrednim uruchomieniu danego pliku

# jesli taki plik zostanie zaimportowany to wykona się tylko
# jego część poza blokiem if __name__ == '__main__'

# ex77_name_main.py
