teller = 2
if teller in [2, 4, 6, 8, 10]:
    print(f"Teller {teller} is even")
if teller not in [2, 4, 6, 8, 10]:
    print(f"Teller {teller} is oneven")

if teller in [2, 4, 6, 8, 10]:
    print(f"Teller {teller} is even")
else:
    print(f"Teller {teller} is oneven")

if teller in [2, 4, 6, 8, 10]:
    print(f"Teller {teller} is even en kleiner dan 10")
elif teller in [12, 14, 16, 18, 20]:
    print(f"Teller {teller} is even en groter dan 10")
else:
    print(f"Teller {teller} is oneven")