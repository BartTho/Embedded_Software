# Slicing
device = "Raspberry Pi"
start = 4
einde = 8 + 1 # +1 omdat het excusief het einde is.
deel = device[start:einde]
print(deel)

deel = device[:einde]
print(deel)

deel = device[start:]
print(deel)

# Raspberry Pi => i=-1, P=-2,y=-4... b=-8
deel = device[-8:]
print(deel)

spring = 2
deel = device[start:einde:spring]
print(deel)

spring = 2
deel = device[start::spring]
print(deel)

spring = 2
deel = device[::spring]
print(deel)