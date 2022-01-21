'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''
lista = []
for szam in range(3):
  bekeres = input("Kérek egy szót!\t")
  lista.append(bekeres)

def legrovidebb(lista,kicsi=lista[0]):
  for szo in lista:
    if len(szo) < len(kicsi):
      kicsi = szo
    
  print(f"A legrövidebb szó: {kicsi}")


print(legrovidebb(lista))
