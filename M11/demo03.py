log = []

with open("kernel.log") as bestand:
    regel = bestand.readline()

    while regel:
        log.append(regel[27:-1])
        regel = bestand.readline()

log.sort()

out = []
aantal = 0
soort = log[0][:log[0].find(" ")]

for logRegel in log:
    if logRegel[:logRegel.find(" ")] == soort:
        aantal += 1
    else:
        out.append([soort, aantal])
        soort = logRegel[:logRegel.find(" ")]
        aantal = 1

out.append([soort, aantal])
print(out)