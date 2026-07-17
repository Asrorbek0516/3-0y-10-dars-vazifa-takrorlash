# Foydalanuvchidan uch tomon uzunligini kiritish
a = float(input("1-tomonni kiriting: "))
b = float(input("2-tomonni kiriting: "))
c = float(input("3-tomonni kiriting: "))

if a < b + c and b < a + c and c < a + b and a!=0 and b!=0 and c!=0:
    print("Uchburchak tuzish mumkin.")
else:
    print("Uchburchak tuzish mumkin emas.")
