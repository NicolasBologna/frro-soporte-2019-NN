# Implementar la función es_primo(), que devuelva un booleano en base a
# si numero es primo o no.


def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

assert es_primo(4) == False
assert es_primo(1) == False
assert es_primo(2) == True
assert es_primo(5) == True
assert es_primo(7) == True
assert es_primo(8) == False
