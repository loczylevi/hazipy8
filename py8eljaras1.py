'''
1. Feladat
Írj eljárást, amely egy tetszőleges szöveget, ill. alakzatot ír ki a képernyőre!
'''
def rajz_udv(a,nev):
  for i in range (1, 8):
    print(a)
    a = a + "*" 
  print(f"""
Üdv a fedélzeten {nev}! argh!""")

print(rajz_udv(a = "*",nev="Pityu"))




