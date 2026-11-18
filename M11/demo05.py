# SET klinkers -> Een set is een collectie waarin elk afzonderlijk element slechts éénmaal kan
# worden opgeslagen
klinkers = {"a","e","i","o","u"}
kwadraten = set(x**2 for x in range(10))

print(klinkers)
print(kwadraten)

# Er is geen manier om te bepalen in welke volgorde je de elementen te zien krijgt
# Je kan de elementen van een set niet sorteren.
kwadraten.add(100)
kwadraten.remove(0)
for x in kwadraten:
    print(x)