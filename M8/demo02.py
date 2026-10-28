device = "Raspberry Pi"

print("#"*60)
pos_letter = 0
while pos_letter < len(device):
    print(device[pos_letter])
    pos_letter += 1
print("#"*60)
for pos_letter in range(len(device)):
    print(device[pos_letter])
print("#"*60)