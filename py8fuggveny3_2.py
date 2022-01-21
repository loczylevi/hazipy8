'''
3.2 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!

Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! 
Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!
'''

lista = []
print("Adj meg számokat ha végeztél adj negativ számot")
while True:
  bekeres = input("Kérek számokat!\t")
  if 0 >= int(bekeres) :
    break
  else:
    lista.append(int(bekeres))


def harommal_oszthatok(lista):
  eredmeny=0
  for szam in lista:
    if szam % 3 == 0:
      eredmeny = eredmeny + 1
  return eredmeny 
 


meghivo = print(f"Ennyi darab 3-mal osztható szám van: {harommal_oszthatok(lista)} ")
print(meghivo)
