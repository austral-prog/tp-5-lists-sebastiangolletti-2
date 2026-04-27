# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):

    if -len(lista) <= indice < len(lista):
        return  lista[indice]
    else:
        return None

get_element([0,1,2,3],3)