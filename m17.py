import json

with open("kontaklar.json", 'r') as f:
    data = json.load(f)

print(data)