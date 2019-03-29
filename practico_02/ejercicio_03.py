# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.

from random import randint

class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.dni = self.generar_dni();


    def es_mayor_edad(self):
        if self.edad >= 18:
            return True
        return False

    # llamarlo desde __init__
    def generar_dni(self):
        return randint(00000000, 99999999)

    def print_data(self):
        atributos = vars(self)

        print (', '.join("%s: %s" % item for item in atributos.items()))

persona = Persona('Nicolas',22,'H',93,1.76)
persona2 = Persona('Milena',14,'M',52,1.65)

persona.print_data()
persona2.print_data()

assert(persona.es_mayor_edad()) == True
assert(persona2.es_mayor_edad()) == False
