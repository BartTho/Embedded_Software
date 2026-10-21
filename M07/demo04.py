import random
import sys

# Exit code	Meaning
# 0	    Success
# 1	    General error
# 2	    Misuse of shell builtins
# 126	Command invoked cannot execute
# 127	Command not found
# 128	Invalid argument to exit
# 130	Script terminated by Control-C

poging = 0
getal = 0
aantal_pogingen = 2
willekeurig_getal = random.randint(1, 10)

while getal != willekeurig_getal:
    if aantal_pogingen == poging:
        print(f"Niet geraden, het Getal is {willekeurig_getal}")
        sys.exit(1)
    poging += 1
    getal = int(input("Raad een getal tussen 1 en 10:"))

print(f"""Je heb het getal geraden in {poging} pogingen""")