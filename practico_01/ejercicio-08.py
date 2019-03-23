# Implementar la función mitad(), que devuelve la mitad de palabra.
# Si la longitud es impar, redondear hacia arriba.


# hola -> ho
# verde -> ver
def mitad(palabra):
    if len(palabra) % 2 == 0:
        long = len(palabra) // 2
    else:
        long = (len(palabra) // 2)+1
    return palabra[:long]


assert mitad("papa") == 'pa'
assert mitad("papap") == 'pap'
assert mitad("prueba") == 'pru'
assert mitad("hola") == 'ho'
assert mitad("verde") == 'ver'
