# SET
klinkers = {"a", "e", "i", "o", "u"}
kwadranten = {x**2 for x in range(1, 10)}
print(klinkers)
print(kwadranten)

kwadranten.add(100)
kwadranten.remove(4)
print(kwadranten)