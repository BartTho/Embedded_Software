# [[1, 11], [2, 5], [3, 5], [4, 4]]
getallen = [1, 2, 3, 4, 5, 8, 12, 15, 19, 21, 24]
deler = [1,2,3,4]
overzicht =  []

for groep in deler:
    aantal = 0

    for getal in getallen:
        if getal % groep == 0:
            aantal += 1

    overzicht.append([groep, aantal])

print("#"*60)
print(f"Dit is de lijst: {overzicht}")
print("#"*60)