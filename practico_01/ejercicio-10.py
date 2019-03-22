# Implementar las funciones superposicion_x(), que tomen dos listas y devuelva
# un booleano en base a
# si tienen al menos 1 elemento en común.


# se debe implementar utilizando bucles anidados.
def superposicion_loop(lista_1, lista_2):
    for e_1 in lista_1:
        for e_2 in lista_2:
            if e_1 == e_2:
                return True
    return False


# se debe implementar utilizando conjuntos (sets).
def superposicion_set(lista_1, lista_2):
    S1 = set(lista_1)
    S2 = set(lista_2)
    print(S1)
    print(S2)
    return S1.intersection(S2)

assert superposicion_loop(['a','b','c','d','e'],['z','x','y','d']) == True
assert superposicion_loop(['a','b','c','d','e'],['z','x','y','h']) == False
assert superposicion_loop(['a','b','c','h','e'],['z','x','y','h']) == True

assert superposicion_set(['a','b','c','d','e'],['z','x','y','d']) == True
assert superposicion_set(['a','b','c','d','e'],['z','x','y','h']) == False
assert superposicion_set(['a','b','c','h','e'],['z','x','y','h']) == True
