import operator

user = {"voornaam": "Bart", "Achternaam": "Thonissen", "login": "bart", "laatstelogin": "2026-11-12", "aantal": 5}
print(user)
print(user.get("username")) # Output: alice_h

print("#"*60)
print(user.get("username", "Onbekend"))
print(user.get("gender", "Onbekend"))

print("#"*60)
user.update({"aantal": 6, "laatstelogin": "2026-11-18"})
print(user)

print("#"*60)
del user["aantal"]
print(user)

print("#"*60)
for key, value in user.items():
    print(f"{key}: {value}")
print("#"*60)

lijst = {"a": 6, "b": 10, "c": 8, "d": 9}
print(f"totaal: {sum(lijst.values())}")
print(sorted(lijst.items(), key=operator.itemgetter(1), reverse=True))