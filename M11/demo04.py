#from logging import critical
overzicht = []
log = []
logregel = ""

with open("kernel.log","r") as bestand:
    regel = bestand.readline()
    while regel:
        log.append(regel[27:-1]) # -1 de newline weg halen
        regel = bestand.readline()

log.sort()

#logregel = log[0]
#soort = logregel[0: log[0].find(" ")]

aantal = 0
soort = log[0][0: log[0].find(" ")]

for logregel in log:
    print(f"regel {logregel}, soort: {soort}")
    if soort == logregel[0: logregel.find(" ")]:
        aantal += 1
    else:
        overzicht.append([soort, aantal])
        soort = logregel[0: logregel.find(" ")]
        aantal = 1
overzicht.append([soort, aantal])

print("#"*60)
print(f"Dit is de lijst: {overzicht}")
print("#"*60)

#soort = logregel[27: logregel.find(" ", 28)]