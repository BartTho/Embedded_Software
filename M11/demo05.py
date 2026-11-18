deelbaardoor2 = {2,4,6,8,10,12,14,16,18,20}
deelbaardoor3 = {3,6,9,12,15,18}

deelbaardoor2_of_door3 = deelbaardoor2.union(deelbaardoor3)
print(deelbaardoor2_of_door3)
deelbaardoor2_of_door3 = deelbaardoor2 | deelbaardoor3
print(deelbaardoor2_of_door3)

deelbaardoor2_en_NIET_door3 = deelbaardoor2.difference(deelbaardoor3)
print(deelbaardoor2_en_NIET_door3)
deelbaardoor2_en_NIET_door3 = deelbaardoor2 - deelbaardoor3
print(deelbaardoor2_en_NIET_door3)

deelbaardoor2_en_door3 = deelbaardoor2.intersection(deelbaardoor3)
print(deelbaardoor2_en_door3)
deelbaardoor2_en_door3 = deelbaardoor2 & deelbaardoor3
print(deelbaardoor2_en_door3)