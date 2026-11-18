getallen = [1, 2, 3, 4, 5, 8, 12, 15, 19, 21, 24]
deelbaardoor2 = []
deelbaardoor3 = []

for getal in getallen:
    if getal % 2 == 0:
        deelbaardoor2.append(getal)
    if getal % 3 == 0:
        deelbaardoor3.append(getal)

print("#"*60)
print(f"Deelbaar door 2 : {deelbaardoor2}")
print("#"*60)
print(f"Deelbaar door 3 : {deelbaardoor3}")
print("#"*60)