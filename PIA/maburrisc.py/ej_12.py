def mitjana(hola):
    suma = 0
    for i in hola:
        suma +=i
    return suma / len(hola)

print(mitjana(range(0,11)))

