'''
5.2 Feladat
A program, egy eljárás segítségével kirajzol a képernyőre egy 6x3-as mezőt. Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)

    O O O O + O
    O O O O O O
    O O O O O O

Feladat
Alakítsd át az előző programot úgy, hogy a felhasználó adhassa meg a koordinátákat, ahová a program 'O' helyett '+' jelet ír. A koordináták bekérése és a mező kirajzolása addig ismétlődjön, amíg a felhasználó negatív számot nem ad meg koordinátaként!
'''
def mezot_rajzol():
  while True:
    szel = int(input("Kérem a szélességet! "))
    if szel < 0:
      print("<<< Program vége <<<")
      break
    hossz = int(input("Kérem a hosszúságot "))
    if hossz < 0:
      print("<<< Program vége <<<")
      break
    for sor in range(3):
        for oszlop in range(6):
          if oszlop == hossz and szel == sor:
            print('+ ', end='')
            
          else:
            print('0 ', end='')
            
        print()
mezot_rajzol()
