shaharlar = {"TOS": "Toshkent", "SAM": "Samarqand", "BUX": "Buxoro"}

belgi = input("kalitni kiriting: ")

for shahar in shaharlar.items():
    if shahar[0] == belgi:
        print(shahar[1])

if shahar[0] != belgi:
    print("Bunday qiymat yuq")
