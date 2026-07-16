yil = int(input("yilni kiriting: "))

if yil % 4 ==0 and (yil % 400 ==0 or yil % 100 != 0):
    print("Bu yil kabisa")
else:
    print("Bu yil kabisa emas")

