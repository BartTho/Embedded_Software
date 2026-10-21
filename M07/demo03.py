import random

punten = 6
getal = 0
te_raden_getal = random.randint(1,10)

while (getal != te_raden_getal) and (punten != 0):
    getal = int(input(f"Raad het getal tussen 1 en 10 je hebt nog {punten} pogingen: "))
    punten -= 1

print(f"Uw score is {punten} !")
