'''
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!
'''

def melyik_nagyobb(num1,num2):
  if num1 > num2:
    print(f"Ez a szám: {num1} a nagyobb!")
  elif num2 > num1:
    print(f"Ez a szám: {num2} a nagyobb!")
  else:
    print("A két szám egyenlő!")

print(melyik_nagyobb(num1 = int(input("Kérek egy számot uram!\t")),num2 = int(input("Kérek egy másik számot uram!\t"))))
