# Implementar la función operacion, donde:
# - Si multiplicar es True: devolver la multiplicación entre a y b.
# - Si multiplicar es False: devolver la division entre a y b.
# - Si multiplicar es False y b es cero: imprimir por consola "Operación no valida".


def operation(a, b, multiplicar):
    if multiplicar == True:
        return a*b
    elif multiplicar == False and b == 0:
        print('Operación no válida')
    else:
        return a/b

assert operation(5, 2, True) == 10
assert operation(5, 5, True) == 25
assert operation(5, 5, False) == 1
assert operation(10, 5, False) == 2
assert operation(0, 5, False) == 0
print('5/0 = ',end="")
operation(5, 0, False)




