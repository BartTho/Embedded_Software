waar = 8 > 2
if waar == True:
    print("Waar")

if waar:
    print("Waar")

# OR
# False - False = False
# True - False = True
# False - True = True
# True - True = True

if waar or 10 > 5:
    print("OR: Waar")

# AND
# False - False = False
# True - False = False
# False - True = False
# True - True = True

if waar and 10 > 5:
    print("AND: Waar")
