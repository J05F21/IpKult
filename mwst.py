def brutto(netto, ermaessigt):
    if ermaessigt == True:
        return netto * 1.07
    else: 
        return netto * 1.19
    
print(brutto(100, True))
    
     
