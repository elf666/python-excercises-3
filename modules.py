# modulem jest kazdy plik z rozszerzeniem .py
# modul po zaladowaniu zachowuje sie jak czesc pliku, do ktorego go zaladowalismy
# importowany modul sam moze importowac kolejne moduly

# import module1 # przy tym sposobie importowania musimy powolywac sie na nazwe modulu
# from module1 import *
# print("I'm in main file")

# module1.function_one()    # importowanie funkcji z modulu
# module1.function_two()
# module1.function_three()  # importowanie funkcji z modulu, ktory importuje inny modul

# def function_one():
#     print("I'm function_one from modules.py")

# from module1 import * # przy tym sposobie importowania mamy dostep bezposredni do nazw
#                       # ale mozemy nadpisac swoje wlasne funkcje!
#
# function_one()
# function_two()
# function_three()


# from module1 import function_one, function_two, function_three
# # w tym sposobie importowania podajemy dokladnie ktore elementy chcemy zaimportowac
#
# function_one()
# function_two()
# function_three()

from module1 import function_one as f1
function_one()
f1()

# ex75_modules.py
# ex76_modules.py
