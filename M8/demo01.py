device = "Raspberry Pi"
print(f"De 5de letter is: {device[4]}")
print(f"Het woord heeft {len(device)} tekens")
# Voorlaatste is "lengte - 2"
# => We beginnen te tellen vanaf 0
# => 12 tekens = 0 tot 11 -> 12 - 2 = 10
print(f"De voorlaatste letter is: {device[len(device)-2]}")
print(f"In de ascii tabel staat op positie 64 het {chr(64)} teken")
print(f"a staat op plaats {ord('a')} en A staat op de {ord('A')} plaats")