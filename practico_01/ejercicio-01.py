# 1. Implementar una función max() que tome como argumento dos números y devuelva el mayor de ellos. 


def maximo(a, b):
    if a != b:
        if a < b:
            return b
        return a
    return a


assert maximo(10, 2) == 10
assert maximo(3,12) == 12
assert maximo(4,4) == 4
