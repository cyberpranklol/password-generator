import random
# varijable = array []
slova = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
brojevi = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simboli = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#poruka
print("Dobrodosli u generator sifre!")
#varijable
nr_slova= int(input("Koliko slova zelite da vasa sifra sadrzi?\n"))
nr_simboli = int(input(f"Koliko simbola zelite?\n"))
nr_brojevi = int(input(f"Koliko brojeva zelite?\n"))

#varijabla
sifra = ""

for char in range(1, nr_slova + 1):
    sifra += random.choice(slova)

for char in range(1, nr_simboli + 1):
    sifra += random.choice(simboli)

for char in range(1, nr_brojevi + 1):
    sifra += random.choice(brojevi)

print(f"Vasa sifra je: {sifra}")
