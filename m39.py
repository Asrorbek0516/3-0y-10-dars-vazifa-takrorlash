royxat = [10, 20, 30, 40, 50, 60]

juft = [royxat[i] for i in range(len(royxat)) if i%2==0]
toq = [royxat[i] for i in range(len(royxat)) if i%2!=0]

print(toq)
print(juft)