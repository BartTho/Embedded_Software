import random

poging = 0
getal = 0
willekeurig_getal = random.randint(1, 10)

while getal != willekeurig_getal:
    poging += 1
    getal = int(input("Raad een getal tussen 1 en 10:"))

print(f"""Je heb het getal 
        geraden in {poging} pogingen""")