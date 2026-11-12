def ist_positiv(zahl):
    return zahl > 0


print(ist_positiv(5))      # True
print(ist_positiv(-3))     # False
print(ist_positiv(0))      # False (0 ist weder positiv noch negativ)
print(ist_positiv(2.5))    # True
print(ist_positiv(-0.1))   # False
