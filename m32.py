mevalar = {"olma", "banan", "uzum", "shaftoli"}

belgi = input("meva kiriting: ")

for meva in mevalar:
    if meva == belgi:
        print("Bor")
if not belgi in mevalar:
    print("Bu meva yuq")