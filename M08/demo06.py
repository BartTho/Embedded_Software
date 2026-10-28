getal = 3.14159

# Gebruik % operator (old style)
print("Het getal Pi is %f of afgerond %.2f" % (getal, getal))

# Gebruik str.format()
print("Het getal Pi is {} of afgerond {:.2f}".format(getal, getal))

# Gebruik f-string
print(f"Het getal Pi is: {getal} en afgerond: {getal:.2f}")

help(str.count)