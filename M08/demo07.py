# Tuple
# Eens aangemaakt ligt de inhoud van de tuple vast; een tuple is 'imm
lijst1 = ("Debian", "Ubuntu", "RedHat", "Fedora")
print(lijst1)
print(lijst1[1])
print(lijst1[-1])
#lijst1.append("Alpine")
print(len(lijst1))

print("#"*60)
# List
lijst2 = ["Debian", "Ubuntu", "RedHat", "Fedora"]
print(lijst2)
print(lijst2[1])
print(lijst2[-1])
lijst2.append("Alpine")
print(lijst2)
print(len(lijst2))

# Slicing
print("#"*60)
print(lijst2[1:-1])
lijst2.remove("Fedora")
print(lijst2)
lijst2.reverse()
print(lijst2)
lijst2.sort()
print(lijst2)
print(lijst2.index("RedHat"))
del lijst2[1]
print(lijst2)