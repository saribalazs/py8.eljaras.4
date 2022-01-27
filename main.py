'''
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
'''

def hossz():
    if len(tomb[0]) > len(tomb(1)) and len(tomb[0])> len(tomb(2)):
        return f"A leghosszabb szó: {tomb[0]}"
    elif len(tomb[0]) < len(tomb(2)) and len(tomb[1]) < len(tomb(2)):
        return f"A leghosszabb szó: {tomb[2]}"
    elif len(tomb[0]) < len(tomb(1)) and len(tomb[1]) > len(tomb(2)):
        return f"A leghosszabb szó: {tomb[1]}"
    else:
        return "Az összes szó ugyan olyan hosszú!"


tomb = []
for i in range(3):
    szo = input("Kérem adjon meg egy szót!")
    tomb.append(szo)
print(tomb)
print(hossz())

