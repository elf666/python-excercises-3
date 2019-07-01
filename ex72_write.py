# przeczytaj plik abc.txt
# na koncu kazdej linijki dodaj "!"
# zapisz te dane do pliku abc!.txt


with open("abc.txt", 'r') as first_file:
     lines = first_file.read().splitlines()

with open ("abc!.txt", 'w') as second_file:
    for line in lines:
        modified_line = line + '!\n'
        second_file.write(modified_line)

# with open('abc.txt', 'r+') as f:
#     lines = f.read().splitlines()
#     for line in lines:
#         modified_line = line + '!\n'
#         f.write(modified_line)
