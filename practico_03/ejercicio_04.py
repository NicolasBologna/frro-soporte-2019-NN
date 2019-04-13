# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona
import sqlite3

def buscar_persona(id_persona):
    db = sqlite3.connect('usuarios')
    cursor = db.cursor()
    sSQL = 'SELECT * FROM Persona WHERE Persona.IdPersona = (?)'
    pSQL = (id_persona,)

    cursor.execute(sSQL, pSQL)
    per=cursor.fetchone()
    if per == None:
        return False
    else:
        return per



@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', '1988-05-15 00:00:00', 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
