# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes
# condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera
# (basándose en el año actual).

from practico_02.ejercicio_03 import Persona
from datetime import  date


class Estudiante(Persona):

    def __init__(self, carrera, anio, cantidad_materias, cantidad_aprobadas, nombre, edad, sexo, peso, altura):
        super().__init__(nombre, edad, sexo, peso, altura)
        self.carrera = carrera
        self.anio = anio
        self.cantidad_materias = cantidad_materias
        self.cantidad_aprobadas = cantidad_aprobadas

    def avance(self):
        return round((self.cantidad_aprobadas / self.cantidad_materias) * 100, 2)

    # implementar usando modulo datetime
    def edad_ingreso(self):
        return self.edad - (date.today().year - self.anio)


estudiante = Estudiante('Ing en Sistemas', 2016, 36, 17,'Nicolas', 22, 'H', 93, 1.76)
assert (estudiante.avance()) == 47.22
assert (estudiante.edad_ingreso()) == 19
