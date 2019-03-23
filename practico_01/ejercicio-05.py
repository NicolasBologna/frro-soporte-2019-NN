# Implementar la función es_vocal, que reciba un carácter y
# devuelva un booleano en base a si letra es una vocal o no.


# Resolver utilizando listas y el operador in.
def es_vocal(letra):
    vocales = ['a', 'e', 'i', 'o', 'u']
    if letra in vocales:
        return True
    return False

var = input("Ingrese una letra: ")
var = es_vocal(var)
if var == True:
    print("La letra es vocal.")
else:
    print("La letra no es vocal.")


assert es_vocal('a') == True
assert es_vocal('b') == False
