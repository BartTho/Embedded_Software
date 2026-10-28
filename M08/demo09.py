# Geneste reeksen
device_os = (["Pi1", "raspbian"], ["Pi2", "Debian"], ["Pi3", "Ubuntu"])
for pi in device_os:
    for os in pi:
        print(os, end="\t")
    print()

maaktafel_3 = tuple(range(3, 31, 3))
print(maaktafel_3)
maaktafel_3 = list(range(3, 31, 3))
print(maaktafel_3)