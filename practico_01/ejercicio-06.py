# Implementar la función multiplicar() que devuelva el producto de todos los números de una lista.


# [1,2,3,4] -> 24
def multiplicar(lista):
    res = 1
    for element in lista:
        res = res * element
    return res

assert multiplicar([3,5,10,15]) == 2250
