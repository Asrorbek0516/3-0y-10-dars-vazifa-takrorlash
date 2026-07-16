baholar = [75, 88, 92, 65, 78, 95, 70, 83]
yigindi = 0
for i in baholar:
    yigindi += i

ortacha = yigindi/len(baholar)
print(ortacha)

if ortacha < 80:
    print("guruh kuchsiz")
else:
    print("guruh kuchli")