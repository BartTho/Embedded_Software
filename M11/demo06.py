import operator
gebruiker = {"voornaam" : "Bart", "achternaam" : "Thonissen", \
             "login" : "bart", "laatstelogin" : "2026-11-12", \
             "aantal" : 6}

print(gebruiker)
print(gebruiker["voornaam"])
print(gebruiker.get("naam", "onbekend"))
gebruiker.update({"laatstelogin" : "2026-11-18", "aantal" : 8})
print(gebruiker)
del gebruiker["laatstelogin"]
print(gebruiker)
for key, value in gebruiker.items():
    print(f"{key}: {value}")

lijst = {"a":6, "b":10,"c":8,"d":9 }
print(f"totaal: {sum(lijst.values())}")
print(sorted(lijst.items(), key=operator.itemgetter(1), reverse=True))
