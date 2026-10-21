disk_gebruik = 110
disk_totaal = 120
in_gebruik = int(disk_gebruik / disk_totaal * 100)
print(f"We gebruike momenteel {disk_gebruik / disk_totaal * 100} %")

if in_gebruik > 80:
    print(f"WAARSCHUWING: Schijfruimte is kritiek,"
          f" {in_gebruik} % in gebruik")