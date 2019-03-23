# Implementar la función conversor, que ingrese desde la consola grados Celsius
# y los devuelva transformados a Fahrenheit.


def conversor(grados):
    return (grados * 9/5) + 32


var = input("Ingrese la temperatura en grados celsius: ")
var = conversor(int(var))
print("La temperatura en grados fahrenheit es: " + str(var))


