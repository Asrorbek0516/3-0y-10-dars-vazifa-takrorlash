with open("sonlar.txt", 'r') as f:
    data = f.readline()

son_int =map(int,data.split(","))

print(sum(son_int))