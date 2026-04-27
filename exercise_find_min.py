# Ejercicio 6: Encontrar el mínimo en una lista

def find_min(lista):
    if len(lista) > 0:
        return min(lista)
    else:
        return None
find_min([-5, 4, 3])
