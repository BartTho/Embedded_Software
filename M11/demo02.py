getallen = [1, 2, 3, 4, 5, 8, 12, 15, 19, 21, 24]
deler =[]
ingelezen = 1
while ingelezen > 0:
    ingelezen = int(input("Geen een deler in:"))
    deler.append(ingelezen)

for groep in deler:
    aantal = 0

    for getal in getallen:
        if getal % groep == 0:
            aantal += 1

    print("#"*60)
    print(f"Er zijn {aantal} getallen deelbaar door {groep}")
    print("#"*60)