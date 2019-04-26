# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime
import sqlite3

from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_06 import reset_tabla
from practico_03.ejercicio_04 import buscar_persona



def agregar_peso(id_persona, fecha, peso):

    db = sqlite3.connect('usuarios')
    cursor = db.cursor()

    def insertar():
        cSQL = 'INSERT OR IGNORE INTO PersonaPeso(IdPersona,Fecha,Peso) VALUES (?,?,?)'
        tdatos = (id_persona, fecha,peso)
        cursor.execute(cSQL, tdatos)
        id =  cursor.lastrowid
        db.commit()
        db.close()
        return id
    if buscar_persona(id_persona):
        cSQL = "SELECT MAX(PersonaPeso.Fecha) FROM PersonaPeso WHERE PersonaPeso.IdPersona = (?)"
        tdatos = (id_persona,)
        cursor.execute(cSQL,tdatos)
        ult_fecha=cursor.fetchone()

        if  (ult_fecha[0] is not None):
            if (datetime.datetime.strptime(ult_fecha[0], '%Y-%m-%d %H:%M:%S') <= fecha):
                return insertar()
        elif (ult_fecha[0] is None):
            return insertar()
    return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()
