# Implementar la función organizar_estudiantes() que tome como parámetro
# una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de
# estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante

est1 = Estudiante('ISI', 2016, 36, 17,'Nicolas', 22, 'H', 93, 1.76)
est2 = Estudiante('ISI', 2014, 36, 26,'Lucas', 24, 'H', 90, 1.80)
est3 = Estudiante('IQ', 2015, 32, 29,'Facundo', 30, 'M', 80, 1.40)
est4 = Estudiante('IM', 2011, 37, 14,'Rodrigo', 20, 'H', 90, 1.80)

estudiantes = [est1,est2,est3,est4]

dicc = {}

def organizar_estudiantes(estudiantes):
    for est in estudiantes:
        if est.carrera in dicc:
            dicc[est.carrera] += 1
        else:
            dicc[est.carrera] = 1

    return dicc

assert(organizar_estudiantes(estudiantes)) == {'ISI': 2, 'IQ': 1, 'IM': 1}

