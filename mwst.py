def brutto(netto, ermaessigt=False):
    if ermaessigt:
        return netto * 1.07
    return netto * 1.19


print(brutto(100))      
print(brutto(10))       
print(brutto(49.99))    
print(brutto(0))         

print(brutto(100, True))             
print(brutto(10, ermaessigt=True))    
print(brutto(100, ermaessigt=False))  
print(brutto(100, 1))               
print(brutto(100, ""))           
