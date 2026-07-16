son  = int(input("son kirting: "))

try:
    natija = 100 / son
    if son == 0:
        print("0 ga bolib bolmaydi")

except ZeroDivisionError:
    print("0 ga bolib bolmaydi")