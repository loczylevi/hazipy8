'''
3.1 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''
"""
lista = []
print("Adj meg számokat ha végeztél nyomj entert!")
while True:
  bekeres = input("Kérek számokat!\t")
  if bekeres == "":
    break
  else:
    lista.append(int(bekeres))
"""

def harommal_oszthatok(*args):
  eredmeny=0
  for szam in args:
    if szam % 3 == 0:
      eredmeny = eredmeny + 1
  return eredmeny 
 
  print(f"Ennyi darab 3-mal osztható szám van: {eredmeny}")


meghivo = harommal_oszthatok(1,2,3,4,5,6,7,8,9,12)
print(meghivo)



