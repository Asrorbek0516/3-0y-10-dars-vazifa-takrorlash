toq = []
juft = []

while True:
    son = int(input("son= "))

    if son == 0:
        break
    
    if son>0:
        juft.append(son)

    else:
        toq.append(son)

print("juftlar yigindi", sum(juft))
print("toqlar yigindi", sum(toq))
    
