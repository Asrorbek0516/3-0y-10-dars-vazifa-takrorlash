try:
    parol = input("parol kiriting: ")
    if len(parol)>8:
        print("Muvaffaqiyatli")

    else:
       print("8 ta belgidan kop bolish kerak parol")

except ValueError:
    print("8 ta belgidan kop bolish kerak parol")
