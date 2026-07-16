from functools import reduce

sonlar = [2, 3, 4, 5]

kopaytma = reduce(lambda a,b: a*b,sonlar)

print(kopaytma)