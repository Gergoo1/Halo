print("1. verzió")
szam = 0
for_in range(100): # A for bejáró ciklus, nem összetévesztendő a for számláló ciklussal!
szam = szam + 1
print(szam,end=" ") # end megváltoztattom az alapértelmezett /n hatását!
print() # A kiiratás a következő sorban kezdődik!

print("2. verzió")
szam = 1
for_in range(100): 
print(szam,end=" ") 
szam = szam + 1
print()

print("3. verzió")
szam = 1
for_in range(1,101): 
szam = szam + 1
print(szam,end=" ") 
print()

print("4. verzió")
szam = 0
for_in range(1,101,1): # _ nem használt változó, de használata lehetséges! print(_)
szam = szam + 1
print(szam,end=" ") 
print()

print("5. verzió")
szam = 0
for_in range(5,105,1): 
szam = szam + 1
print(szam,end=" ") 
print()

print("6. verzió")
for_in range(100): # A szam = 0,1,...98,99
print(szam + 1,end=" ") 
print()