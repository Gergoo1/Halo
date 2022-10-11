egyikszam=int(input("Kérem az első számot 1-100-ig"))
egyikszam=int(input("Kérem az másik számot 1-100-ig"))
if egyikszam<masikszam:
    print("A második szám nagyobb")
    print("Ennyivel:",masikszam-egyikszam)
elif egyikszam>masikszam:
    print("Az első szám nagyobb")
    print("Ennyivel:",egyikszam-masikszam)
else:
    print("megegyezik")