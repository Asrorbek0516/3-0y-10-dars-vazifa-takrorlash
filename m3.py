sonlar = []

for i in range(5):
    son = int(input(f"{i+1} sonni kiriting: "))

    sonlar.append(son)

print(sonlar)

max = sonlar[0]
min = sonlar[0]

for son in sonlar:
    if son>max:
        max = son
    if son<min:
        min = son

print("kattasi= ",max)
print("kichigi = ",min)