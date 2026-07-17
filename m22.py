
sozlar = []
for i in range(5):
    soz = input(f"{i+1}-so'zni kiriting: ")
    sozlar.append(soz)

for i in range(len(sozlar)):
    for j in range(i+1, len(sozlar)):
        if len(sozlar[i]) < len(sozlar[j]):
            sozlar[i], sozlar[j] = sozlar[j], sozlar[i]

for s in sozlar:
    print(s)
