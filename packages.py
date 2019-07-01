# pakiet jest folderem, ktory zawiera w sobie jeden lub wiecej modulow
# oraz plik __init__.py
# plik ten jest KONIECZNY aby poinformowac Pythona, ze dany folder jest pakietem
# plik __init__.py moze, ale nie musi byc pusty

# importowanie metoda 1
from my_package import module_in_package

module_in_package.function_four()

# importowanie metoda 2
import my_package.module_in_package

my_package.module_in_package.function_four()

# importowanie z uzyciem as
import my_package.module_in_package as m1
m1.function_four()

from my_package.module_in_package import function_four
function_four()

from my_package.module_in_package import function_four as function_x
function_x()

# ex78_packages.py

# wiecej o __init__.py
#
# __init__.py MOZE byc pusty i w tej roli słuzy jedynie do poinformowania Pythona,
# ze dany folder jest pakietem

# __init__.py moze rowniez zawierac wewnętrzną konfiguracje, np.:
# from .modul import funkcja
# from pakiet.moduł import funkcja
# (konieczna kropka lub nazwa pakietu, poniewaz Python
# bedzie szukał nazwy modułu w katalogu, z ktorego uruchamiamy skrypt!)
# parametr __all__ = ['modul1', 'modul2']
# pozwala podac liste modulow, ktore maja byc automatycznie
# zaladowane przy from pakiet import *

# sprojmy przetestowac to na pakiecie matematyka

from matematyka import *

print(pomnoz_a_przez_b(10,20))
print(pole_trapezu(10,20,30))

# print(algebra.pomnoz_a_przez_b(10,20))
# print(geometria.pole_trapezu(10,20,30))

# ex_79_packages.py
