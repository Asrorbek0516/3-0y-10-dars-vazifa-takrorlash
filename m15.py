son = int(input("narx kiriting: "))

if son > 100000:
    print(son-(son *20/100))

elif 50000 < son < 100000:
    print(son-(son*10/100))

else:
    print("Chegirma yuq")