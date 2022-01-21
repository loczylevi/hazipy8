'''
2. Feladat
Írj egy programot, amely tartalmaz egy 'paros_e' nevű függvényt, amely True értékkel tér vissza, ha a paraméterként átvett listaelemek (egész számok) között van páros, ellenkező esetben a visszatérési érték False! 
A program tartalmazza a függvény hívását is!
'''

lista = []
print("Adj meg számokat ha végeztél nyomj entert!")
while True:
  bekeres = input("Kérek számokat!\t")
  if bekeres == "":
    break
  else:
    lista.append(int(bekeres))

def paros_e(lista):
  for szam in lista:
    if szam % 2 == 0:
      return True
    else:
      return False

meghivo = paros_e(lista)
print(meghivo)

