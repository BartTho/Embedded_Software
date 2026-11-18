getallen = [1,2,3,4,5,8,12,15,19,21,24]

deler = []
out = []

ingelezen = 1
while ingelezen > 0:
    ingelezen = int(input("Geef een deler in, stop met een negatief getal: "))
    deler.append(ingelezen)

deler = deler[:-1]

for groep in deler:
    aantal = 0

    for getal in getallen:
        if getal % groep == 0:
            aantal += 1
    out.append([groep, aantal])

print(f"#"*60)
print(out)
print(f"#"*60)