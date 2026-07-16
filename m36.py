import json

with open("talabalar.json", 'r') as file:
    data = json.load(file)
katta_baho = data[0]
for talaba in data:
    if talaba["baho"]>katta_baho["baho"]:
        katta_baho = talaba

print(f"{katta_baho['ism']} - {katta_baho['baho']}")

