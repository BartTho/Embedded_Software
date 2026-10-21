border = '#' * 60
print(border)
print(f"{'Iteraties':^60}")
print(border)

for teller in range(10):
    print(f"Waarde van de teller = {teller + 1}")

print(border)
for teller in range(1, 11): # 1 tot 10, 11 niet
    print(f"Waarde van de teller = {teller}")

print(border)
for teller in range(10, 0, -1): # 1 tot 10, 11 niet
    print(f"Waarde van de teller = {teller}")

print(border)
print(f"{'Einde':^60}")
print(border)