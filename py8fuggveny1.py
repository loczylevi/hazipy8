'''
1. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket (egész számokat) összeadja és az összegükkel tér vissza! 
A program tartalmazza a függvény hívását is!
'''


def osszegzo(*args):
    x = 0
    for szam in args:
        x += szam
        
    return x
fuggvenyhivas = osszegzo(1,2,3,4,5,6,7,8,9)
print(fuggvenyhivas)
