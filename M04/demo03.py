# Een auto rijdt met een snelheid van 50km/h. Wat is de afgelegde afstand na 5 minuten
snelheid = int(input("Wat is de snelheid:"))
tijd = int(input("Wat is de tijd:"))
afstand = (snelheid / 60 * tijd)

print(type(str(tijd)))
# int() float() str()
# print(afstand)
#print("De auto rijdt " + str(afstand) + " km in" + str(tijd) + " minuten")
#print("De auto rijdt ", afstand, " km in", tijd, " minuten")
print(f"De auto rijdt {afstand} km in {tijd} minuten")
print(f"De auto rijdt {int(afstand)} km in {tijd} minuten")