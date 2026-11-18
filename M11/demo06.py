deelbaardoor2 = {2,4,6,7,8,10,12,14,16,18,20}
deelbaardoor3 = {3,6,9,12,15,18}

deelbaardoor2of3 = deelbaardoor2.union(deelbaardoor3)
print(deelbaardoor2of3)
deelbaardoor2enNIETdoor3 = deelbaardoor2.difference(deelbaardoor3)
print(deelbaardoor2enNIETdoor3)
deelbaardoor2endoor3 = deelbaardoor2.intersection(deelbaardoor3)
print(deelbaardoor2endoor3)

deelbaardoor2of3 = deelbaardoor2 | deelbaardoor3
print(deelbaardoor2of3)
deelbaardoor2enNIETdoor3 = deelbaardoor2 - deelbaardoor3
print(deelbaardoor2enNIETdoor3)
deelbaardoor2endoor3 = deelbaardoor2 & deelbaardoor3
print(deelbaardoor2endoor3)