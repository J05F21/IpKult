def brutto(netto, ermaessigt=False):
    if ermaessigt:
        return netto * 1.07
    return netto * 1.19


# a) Normaler Steuersatz (19 %)
print(brutto(100))       # 119.0
print(brutto(10))        # 11.899999999999999 (Rundungsfehler bei Kommazahlen)
print(brutto(49.99))     # 59.4881
print(brutto(0))         # 0.0

# b) Ermäßigter Steuersatz (7 %)
print(brutto(100, True))              # 107.0
print(brutto(10, ermaessigt=True))    # 10.700000000000001
print(brutto(100, ermaessigt=False))  # 119.0
print(brutto(100, 1))                 # 107.0 (1 ist truthy)
print(brutto(100, ""))                # 119.0 ("" ist falsy)
