'''
2. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
'''

def negativ_pozitiv(num):
  if num > 0:
    print(f"Ez a szám --> {num} POZITIV!")
  elif num < 0:
    print(f"Ez a szám --> {num} NEGATIV!")
  else:
    print("Ez a szám a NULLA!")

negativ_pozitiv(num=int(input("Kérek egy számot uram!\t")))

