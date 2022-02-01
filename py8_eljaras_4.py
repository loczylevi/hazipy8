'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''
def legkisebb(*szavak):
  legkisebb = szavak[0]
  for szo in szavak:
    if szo > legkisebb:
      legkisebb = szo 
  print(f" A legkisebb szó: {legkisebb}")
legkisebb("alma","alapocska","fa")
