# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime
import sqlite3

from practico_03.ejercicio_01 import reset_tabla
from practico_03.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):

    db = sqlite3.connect('usuarios')
    cursor_borrar = db.cursor()
    cSQL = "DELETE FROM Persona WHERE Persona.IdPersona = (?)"
    tdatos = (id_persona,)

    cursor_borrar.execute(cSQL, tdatos)
    if(cursor_borrar.rowcount):
        db.commit()
        db.close()
        return True
    else:
        db.close()
        return False
#prueba git
@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
