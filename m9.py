file = "mevalar.txt"

with open(file, 'r') as f:
    data = f.readlines()
    data = list(map(lambda s:s.strip("\n"), data))

print(data)