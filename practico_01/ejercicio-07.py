# Implementar la función numeros_al_final(), que mueve todos los elementos numéricos
# de lista al final de esta. Devuelve la lista.


# Resolver sin utilizar lista auxiliar
def numeros_al_final(lista):
    i = 0
    long = (len(lista) - 1)
    while i < long:
        if lista[i].isnumeric():
            lista.append(lista[i])
            lista.remove(lista[i])
            i -= 1
            long -= 1
        i += 1
    return lista

assert numeros_al_final(['a','4','e','h','3','4','j','R','2']) == ['a', 'e', 'h', 'j', 'R', '2', '4', '3', '4']
assert numeros_al_final(['1','4','e','h','3','4','j','R','2']) == ['e', 'h', 'j', 'R', '2', '1', '4', '3', '4']
assert numeros_al_final(['99','4','e','9','y','y','3','t','j','R','2','0']) == ['e', 'y', 'y', 't', 'j', 'R', '0', '99', '4', '9', '3', '2']

