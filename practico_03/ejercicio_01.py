# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

import sqlite3

def crear_tabla():
    db = sqlite3.connect('Usuarios')

    cursor = db.cursor()

    cSQL = 'CREATE TABLE IF NOT EXISTS Persona(IdPersona INTEGER PRIMARY KEY AUTOINCREMENT , Nombre VARCHAR(30), FechaNacimiento DATE, Dni INT, Altura INT)'

    cursor.execute(cSQL)

    db.commit()

    db.close()


def borrar_tabla():
    db = sqlite3.connect('Usuarios')

    cursor = db.cursor()

    cSQL =  'DROP TABLE IF EXISTS Persona'

    cursor.execute(cSQL)

    db.commit()

    db.close()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

borrar_tabla()
