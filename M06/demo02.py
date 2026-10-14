waar = 8>2
if waar == True:
    print("OK")

waar = 8>2
if waar:
    print("OK")

# OR
# False - False = False
# False - True = True
# True - False = True
# True - True = True

if disk_gebruik > 90 or waar:
    print("OK")

# AND
# False - False = False
# False - True = False
# True - False = False
# True - True = True

if disk_gebruik > 90 and waar:
    print("OK")