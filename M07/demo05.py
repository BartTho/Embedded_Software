getal = 0
tafel = 0
for a in range(10):
    tafel += 1
    getal = 1
    for b in range(10):
        print(f" {(getal)*(tafel)}", end='\t')
        getal += 1
    print()