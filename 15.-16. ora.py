# bekérünk két egész számot és irassuk ki a nagyobb számot
"""
szam_1=int(input("Kérek egy egész számot: "))
szam_2=int(input("Kérek még egy egész számot: "))

if szam_1 > szam_2: 
   print("Az első szám nagyobb")
if szam_2 > szam_1:
    print("A második szám nagyobb")
if szam_1==szam_2:
    print("A két szám megegyezik")
"""

"""
szam_1=int(input("Kérek egy egész számot: "))
szam_2=int(input("Kérek még egy egész számot: "))

if szam_1 > szam_2: 
   print("Az első szám nagyobb")
elif szam_2 > szam_1:
    print("A második szám nagyobb")
elif szam_1==szam_2:
    print("A két szám megegyezik")
 """

 a=int(input("Kérek egy egész számot:"))
 b=int(input("Kérek egy egész számot:"))
 c=int(input("Kérek egy egész számot:"))
 if a < b and c > b:
    print("a kisebb mint b és c nagyobb mint b")
else:
    print("A feltétel hamis")