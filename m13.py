import random

son  = random.randint(1,100)
count = 0

while count< 5:
    count +=1
    taxmin = int(input("Son kiriting: "))

    if son == taxmin:
        print(f"{count} ta uriniushda topdingiz {son}")

    if taxmin < son:
        print("Kattaroq")

    if taxmin > son:
        print("Kichikroq")

else:
    print(f"Afsuski sz topolmadingiz o'ylangan son {son}")